import streamlit as st
import time

st.set_page_config(page_title="Infinite Pi Streamer")
st.title("Infinite Pi Generator")
st.write("This algorithm calculates the digits of Pi one by one.")

# The Generator Algorithm
def calcPiInfinite():
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    while True:
        if 4 * q + r - t < n * t:
            yield n
            nr = 10 * (r - n * t)
            n = ((10 * (3 * q + r)) // t) - 10 * n
            q *= 10
            r = nr
        else:
            nr = (2 * q + r) * l
            nn = (q * (7 * k) + 2 + (r * l)) // (t * l)
            q *= k
            t *= l
            l += 2
            k += 1
            n = nn
            r = nr

# UI Layout
placeholder = st.empty()
full_pi = ""

if st.button('Start Generating'):
    count = 0
    for digit in calcPiInfinite():
        if count == 1:
            full_pi += "."
        
        full_pi += str(digit)
        
        # Update the screen with the new digit
        placeholder.code(full_pi)
        
        count += 1
        time.sleep(0.05) # Slows it down so you can see it happen
