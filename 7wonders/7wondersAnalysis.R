# -----------------------
# Load data and libraries
# -----------------------
library(reshape)
library(ggplot2)
library(plotly)
library(gridExtra)
data <- read.csv("games.csv",header=TRUE)
data_melt <- melt(data, id=c("gameID","player","num_players","rank"))

# ------------
# violin plots
# ------------
overall_violin <- ggplot(data=data_melt,aes(x=variable,y=value)) + 
    geom_violin(aes(fill=variable))+
    geom_boxplot(width=0.05)+
    scale_fill_manual(values=c("#ff5447","#ffd770","#ffffff","#21aeff","#fffc63","#d063ff","#80ff63","#000000"))+
    theme(legend.position = "none")+
    xlab("Point Category")+
    ylab("Number of Points")+
    ylim(-6,68)+
    ggtitle("Overall Point Distribution (N=133)")

my_violin <- ggplot(data=data_melt[data_melt$player == "Me",],aes(x=variable,y=value)) + 
    geom_violin(aes(fill=variable))+
    geom_boxplot(width=0.05)+
    scale_fill_manual(values=c("#ff5447","#ffd770","#ffffff","#21aeff","#fffc63","#d063ff","#80ff63","#000000"))+
    theme(legend.position = "none")+
    xlab("Point Category")+
    ylab("Number of Points")+
    ylim(-6,68)+
    ggtitle("My Point Distribution (N=32)")

dad_violin <- ggplot(data=data_melt[data_melt$player == "Dad",],aes(x=variable,y=value)) + 
    geom_violin(aes(fill=variable))+
    geom_boxplot(width=0.05)+
    scale_fill_manual(values=c("#ff5447","#ffd770","#ffffff","#21aeff","#fffc63","#d063ff","#80ff63","#000000"))+
    theme(legend.position = "none")+
    xlab("Point Category")+
    ylab("Number of Points")+
    ylim(-6,68)+
    ggtitle("Dad's Point Distribution (N=24)")

combined_violin <- grid.arrange(overall_violin,my_violin,dad_violin,ncol=1)

# ----------
# Bar Graphs
# ----------
ranks <- data.frame("none",0,0)
names(ranks) <- c("player","rank","occurences")
for(name in unique(data$player)){
    for(rank in seq(1,7)){
        row <- c(name,rank,nrow(data[data$player==name & data$rank==rank,]))
        ranks <- rbind(ranks,row)
    }
}
ranks <- ranks[-1,]
ranks <- ranks[ranks$player %in% c("Me","Dad","Mom","Matt"),]
ranks$player <- factor(ranks$player,levels = c("Me","Dad","Mom","Matt"))
rankings_bar <- ggplot(data=ranks,aes(x=player,y=as.numeric(occurences),fill=rank))+
    geom_bar(stat="identity",position=position_dodge())+
    scale_fill_manual(label=c("1st","2nd","3rd","4th","5th","6th","7th"),values=c("darkgoldenrod1","grey60","#CD7F32","coral4","indianred1","deeppink","purple"))+
    ylab("Frequency")+
    ggtitle("Frequency of Player Ranking (Top 4/29 Players, N=92)")


# -----------------
# Correlation matrix
# -----------------
cormat <- cor(data[,-c(1,2,3,4)])
melted_cormat <- melt(cormat)

correlation_heatmap <- ggplot(data = melted_cormat, aes(x=X1, y=X2, fill=value)) + 
    geom_tile()+
    scale_fill_gradient2(low = "blue", high = "red", mid = "white", 
                         midpoint = 0, limit = c(-1,1), space = "Lab", 
                         name="Pearson\nCorrelation") +
    theme_minimal()+ 
    theme(axis.text.x = element_text(angle = 45, vjust = 1, 
                                     size = 12, hjust = 1),
          axis.title.x = element_blank(),
          axis.title.y = element_blank())+
    ggtitle("Point Category Correlation Matrix (N=133)")+
    coord_fixed()

# --------------------
# Combining everything
# --------------------

lay <- rbind(c(1,2),
                c(1,2),
                c(1,3),
                c(5,3),
                c(5,4),
                c(5,4))

final_combined <- grid.arrange(rankings_bar, overall_violin, my_violin, dad_violin, correlation_heatmap,layout_matrix=lay)
ggsave("./7wonders.png",final_combined, height=10,width=12)
