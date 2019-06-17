library(dplyr)
library(readr)
library(ggplot2)
library(ggrepel)
data <- read_csv('network_attributes.csv') %>% filter(Id != '牙醫學系')

ggplot(data, aes(x = `industr_2nd-3rd`, y = dropRate1061)) +
  geom_point(aes(color = college)) 
  #geom_text_repel(aes(label = Id, color = college))

ggplot(data, aes(x = dropRate1061, y = transfer_pageranks)) +
  geom_point(aes(color = college)) 
cor(data$dropRate1061, data$transfer_pageranks)

ggplot(data, aes(x = dropRate1061, y = ntuApplic_pageranks)) +
  geom_point(aes(color = college)) 
cor(data$dropRate1061, data$ntuApplic_pageranks)



cor(data$`industr_1st-2nd`, data$dropRate1061)
cor(data$`industr_2nd-3rd`, data$dropRate1061)
cor(data$`job_1st-2nd`, data$dropRate1061)
cor(data$`job_2nd-3rd`, data$dropRate1061)



## NTU Application subnetworks

# Whole network
data %>% filter(Id != '牙醫學系') %>%
  ggplot(aes(x = `industr_2nd-3rd`, 
             y = ntuApplic_pageranks)) +
    geom_point(aes(color = college), size = 0.5) +
    geom_text_repel(aes(label = Id, color = college), size = 2) +
    geom_smooth(method = 'lm')
cor(data$ntuApplic_pageranks, data$`industr_2nd-3rd`)


# Arts subnetwork
dataArts <- data %>% filter(isArts) %>% filter(Id != '牙醫學系')
ggplot(dataArts, aes(x = `industr_2nd-3rd`, 
                     y = ntuApplic_arts_pageranks)) +
  geom_point(aes(color = college), size = 0.5) +
  geom_text_repel(aes(label = Id, color = college), size = 2) +
  geom_smooth(method = 'lm')
cor(dataArts$ntuApplic_arts_pageranks, dataArts$`industr_2nd-3rd`)

# Non Arts subnetwork
dataNonArts <- data %>% filter(!isArts) %>% filter(Id != '牙醫學系')
ggplot(dataNonArts, aes(x = `industr_2nd-3rd`, 
                     y = ntuApplic_nonArts_pageranks)) +
  geom_point(aes(color = college), size = 0.5) +
  geom_text_repel(aes(label = Id, color = college), size = 2) +
  geom_smooth(method = 'lm')


cor(dataNonArts$ntuApplic_nonArts_pageranks, dataNonArts$`industr_2nd-3rd`)
