data = readr::read_csv('transfer_attributes.csv')
college = unique(data$college)
college
paste(college, collapse = ')|(')

#(工學院)|(電資學院)|(醫學院)|(文學院)|(管理學院)|(理學院)|(生農學院)|(社科學院)|(法律學院)|(公衛學院)|(生命科學院)

#(工學院)|(電資學院)|(醫學院)|(管理學院)|(理學院)|(生農學院)|(公衛學院)|(生命科學院)