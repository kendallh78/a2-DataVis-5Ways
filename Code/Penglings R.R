if (!requireNamespace("ggplot2", quietly = TRUE)) {
  install.packages("ggplot2")
}

library(ggplot2)

csv_path <- "/Users/kendallhaddigan/Desktop/A2/penglings.csv"

data <- read.csv(csv_path)

# set up the ggplot with the scatter plot
ggplot(data, aes(x = flipper_length_mm, y = body_mass_g, color = species, size = bill_length_mm)) +
  geom_point(alpha = 0.8) +
  
  # background color
  theme(panel.background = element_rect(fill = "#EBEBEB", color = NA)) +
  
  # gridline color
  theme(panel.grid.major = element_line(color = "white", linetype = "solid")) +
  
  # title
  ggtitle("Pengling Body Mass Prediction") +
  
  # x and y axis labels
  xlab("Flipper Length (mm)") +
  ylab("Body Mass (g)") +
  
  # size down dot size 
  scale_size_continuous(range = c(1, 3)) +
  
  # color palette
  scale_color_manual(values = c("Adelie" = "#FBA043", "Chinstrap" = "#9935CC", "Gentoo" = "#469F9F"))

