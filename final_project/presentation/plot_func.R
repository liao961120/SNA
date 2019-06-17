library(ggplot2)
library(ggrepel)
plot_xy <- function(data, x, y, color = data$college,
                    title = NULL,
                    xlab = '工作變動性 (2-5 年 vs. 5-10 年)',
                    ylab = '轉系網絡 PageRank') {
  pl <- ggplot(data, 
               aes(x = x, y = y)) +
    geom_point(aes(color = color), size = 0.5) +
    geom_smooth(se = T, formula = y~x, method='lm', 
                size=0.4, alpha = 0.2) +
    geom_text_repel(aes(label = Id, color = color), 
            size = 2, segment.size = 0.15) +
    labs(title = title,
         x = xlab, #'工作變動性 (2-5 年 vs. 5-10 年)'
         y = ylab) +  #轉系網絡之 PageRank
    theme_bw()+
    theme(legend.position = "none")
}