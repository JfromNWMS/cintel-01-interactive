import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
from shiny.express import input, render, ui

ui.page_opts(title='Random Normalized Histogram', fillable=True)

with ui.sidebar():
    ui.input_slider('selected_number_of_bins', 'Number of Bins', 0, 100, 20)

@render.plot(alt="A histogram showing random data distribution")
def draw_histogram():    
    count_of_points: int = 437
    np.random.seed(19680801)
    random_data_array: np.ndarray = 100 + 15 * np.random.randn(count_of_points)
    plt.hist(random_data_array, input.selected_number_of_bins(), density=True)
