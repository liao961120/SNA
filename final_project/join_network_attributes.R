library(dplyr)
ntu_attr <- readr::read_csv('ntuApplic_attributes.csv')
transfer_attr <- readr::read_csv('transfer_attributes.csv')

ntu_attr <- ntu_attr %>% 
  rename(Id = Label) %>%
  rename(ntuApplic_pageranks = pageranks) %>%
  rename(ntuApplic_degree = Degree) %>%
  rename(ntuApplic_clustering_coefficient = clustering) %>%
  rename(ntuApplic_eigenCentrality = eigencentrality) %>%
  select(-college)

transfer_attr <- transfer_attr %>%
  rename(transfer_indegree = indegree) %>%
  rename(transfer_outdegree = outdegree) %>%
  rename(transfer_degree = Degree) %>%
  rename(transfer_eigenCentrality = eigencentrality)


x = left_join(transfer_attr, ntu_attr, by = c('Id' = 'Id'), keep = T)

x = x %>% 
  mutate(isArts = if_else(college %in% c('文學院', '社科學院','法律學院'),
                          TRUE, FALSE))

readr::write_csv(x, 'network_attributes.csv')