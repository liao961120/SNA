library(dplyr)
library(ggplot2)
library(ggrepel)


arts = readr::read_csv('transfer_Arts_attributes.csv')
nonArts = readr::read_csv('transfer_nonArts_attributes.csv')

ggplot(data = arts, 
       aes(x = `industr_2nd-3rd`, y = pageranks)) +
  geom_point(aes(color=college), size = 0.5) +
  geom_smooth(method = 'lm', se = F, size = 0.3, color='grey') +
  geom_text_repel(aes(label = Id, color=college), size = 2) +
  theme(legend.position = "none")


ggplot(data = nonArts,
       aes(x = `industr_2nd-3rd`, y = pageranks)) +
  geom_point(aes(color=college), size = 0.5) +
  geom_smooth(method = 'lm', se = F, size = 0.3, color='grey') +
  geom_text_repel(aes(label = Id, color=college), size = 2) +
  theme(legend.position = "none")
