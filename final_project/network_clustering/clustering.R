library(dendextend)
library(dplyr)
# Department data
college = readr::read_csv('ntuNetwork_attr2.csv') %>% 
  select(label, college)
# 104 application network clustering
x = read.table('104application_netSE2.csv', header=T, sep=',', row.names = 1)
x = as.matrix(x)

# Clustering: 104 network
clust = hclust(d = as.dist(x), method = "ward.D")
#plot(clust)
clust[['labels']]
groups_104 <- cutree(clust, k=11)
#rect.hclust(clust, k=11, border="red")

# Plot
dendro_104 <- as.dendrogram(clust)
dendro_104 %>% 
  set("branches_k_color", k = 11) %>% 
  set("labels_cex", 0.4) %>%
  set("labels_colors") %>%
  plot(main = "104 學測網絡分群", horiz = T)
  

# 106 department transfer network clustering
y = read.table('transfer_netSE2.csv', header=T, sep=',', row.names = 1)
y = as.matrix(y)
# Clustering: transfer network
clust2 = hclust(d = as.dist(y), method = "ward.D")
#plot(clust2)
clust2[['labels']]
groups_transfer <- cutree(clust2, k=11)
#rect.hclust(clust2, k=11, border="red")
# Plot
dendro_transfer<- as.dendrogram(clust2)
dendro_transfer %>% 
  set("branches_k_color", k = 11) %>% 
  set("labels_cex", 0.4) %>%
  set("labels_colors") %>%
  plot(main = "106 轉系網絡分群", horiz = T)
  


## Combine data
library(dplyr)
groups_104 <- cbind(names(groups_104), groups_104) %>%
  as_tibble()
cluster_results <- cbind(names(groups_transfer), groups_transfer) %>% 
  as_tibble() %>%
  left_join(groups_104, by = c('V1'='V1'), keep=T) %>%
  left_join(college, by = c('V1'='label'), keep=T)


# Dummy matrix
mat_df = read.table('104application_netSE2.csv', header=T, sep=',', row.names = 1)
# Transfer network clustering result matrix
for (rlab in rownames(mat_df)) {
  for (clab in colnames(mat_df)) {
    idx1 = cluster_results$V1 == rlab
    idx2 = cluster_results$V1 == clab
    if (cluster_results$groups_transfer[idx1] == cluster_results$groups_transfer[idx2])
    mat_df[rlab, clab] = 1
    else {mat_df[rlab, clab] = 0}
  }
}
mat_df_transfer = mat_df

# 104 network clustering result matrix
mat_df_104 = mat_df
for (rlab in rownames(mat_df_104)) {
  for (clab in colnames(mat_df_104)) {
    idx1 = cluster_results$V1 == rlab
    idx2 = cluster_results$V1 == clab
    if (cluster_results$groups_104[idx1] == cluster_results$groups_104[idx2])
    mat_df_104[rlab, clab] = 1
    else {mat_df_104[rlab, clab] = 0}
  }
}

# Original college label
#college = readr::read_csv('ntuNetwork_attr2.csv') %>% select(label, college)
mat_df_college = mat_df
for (rlab in rownames(mat_df_college)) {
  for (clab in colnames(mat_df_college)) {
    idx1 = college$label == rlab
    idx2 = college$label == clab
    if (college$college[idx1] == college$college[idx2])
    mat_df_college[rlab, clab] = 1
    else {mat_df_college[rlab, clab] = 0}
  }
}

# Calculate correlation between two matricies
applic_104 = as.vector(as.matrix(mat_df_104))
transfer = as.vector(as.matrix(mat_df_transfer))
collage_label = as.vector(as.matrix(mat_df_college))
cor(applic_104, transfer)
cor(transfer, collage_label)
cor(applic_104, collage_label)


# Save cluster results
readr::write_csv(cluster_results, '2networks_clustering.csv')
