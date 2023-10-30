from src import extraction, transforming, visualization

if __name__ == '__main__':
    extraction.federacion()
    transforming.federacion_cleaning()
    transforming.garmin_cleaning()
    visualization.visualization()
