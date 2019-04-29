dep_info <- readr::read_csv('dept_info.csv')
network_attr <- readr::read_csv('ntuNetwork_attr.csv')

network_attr$college <- ''
for (i in seq_along(dep_info$dept)) {
  matched_dept <- which(grepl(dep_info$dept[i], network_attr$label))
  network_attr$college[matched_dept] <- dep_info$college[i]
}

readr::write_csv(network_attr, 'ntuNetwork_attr2.csv')
