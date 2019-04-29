ori_dir <- getwd()

setwd('~/Desktop/SNA')

files <- list.files(pattern='html$', recursive = T, full.names = T)
file_ext <- function(...) tools::file_ext(...)



out_str <- paste0('<a target="_blank" href="', files, '">', files, '</a><br>')

out_str <- c('', out_str)

writeLines(out_str, con = 'index.html')

setwd(ori_dir)