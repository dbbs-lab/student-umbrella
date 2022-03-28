import numpy as np
import plotly.graph_objs as go
import pickle
import scipy.signal

# Load the data from a saved file, we "know" it contains the time and membrane potential
with open("golgi_trace.pkl", "rb") as g:
    time, signal = pickle.load(g)

# Find the big peaks in the signal
peak_indices, peak_properties = scipy.signal.find_peaks(signal, height=5)
# The indices represent the N-th samples that have been chosen as peaks, so:
# Select the N-th time samples
t_peaks = time[peak_indices]
# And the associated N-th membrane potential samples
v_peaks = signal[peaks]

# Use `plotly` to make a graph object figure, with 2 graph object scatter traces.
go.Figure([
    # Plot the time on the x axis, the membrane potential on Y
    go.Scatter(x=time, y=signal),
    # Plot the peaks as markers
    go.Scatter(x=t_peaks, y=v_peaks, mode="markers"),
]).show()
