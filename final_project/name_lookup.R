data = readr::read_csv('net_data.csv')
View(data)

dept =  sort(unique(c(data$source, data$target)))
View(dept)


library(dplyr)
data2 <- readr::read_csv('104Crawl/job_stability.csv')
data2 <- data2 %>% arrange(dept)

readr::write_csv(data2, '104Crawl/job_stability2.csv')

View(data2)
dept2 = sort(data2$dept)


data3 <- readr::read_csv('104Crawl/ntuNetwork_attr.csv')
dept3 = sort(data3$label)


x = as_tibble(cbind(dept, dept2, dept3))
colnames(x) = c('轉系','104人力銀行','104學測網絡')
readr::write_csv(x, 'name_lookup.csv')
