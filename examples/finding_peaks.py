import numpy as np
import plotly.graph_objs as go
import pickle
import scipy.signal

# Load the data from a saved file
with open("golgi_traces.pkl", "rb") as g:
    golgi_traces = pickle.load(g)

# We "know" that the data contains Golgi cell membrane potential time series under
# the keys 0 to 69, and a special key "time" for the time of all time series.

# So, extract the time, and the traces of a Golgi cell, I picked cell 2, no reason.
t = golgi_traces["time"]
signal = golgi_traces[2]

# Find the big peaks in the signal
peak_indices, peak_properties = scipy.signal.find_peaks(signal, height=5)
# The indices represent the N-th samples that have been chosen as peaks, so:
# Select the N-th time samples
t_peaks = t[peak_indices]
# And the associated N-th membrane potential samples
v_peaks = signal[peaks]

# Use `plotly` to make a graph object figure, with 2 graph object scatter traces.
go.Figure([
    # Plot the time on the x axis, the membrane potential on Y
    go.Scatter(x=t, y=signal),
    # Plot the peaks as markers
    go.Scatter(x=t_peaks, y=v_peaks, mode="markers"),
]).show()
