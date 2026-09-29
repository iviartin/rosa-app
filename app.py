import numpy as np
import streamlit as st
from starter import ZONES, TIME_BLOCKS, COSTS, PROMISE, delivery_times


def LateCost(numlate, costs=COSTS):
    cost_per_late_order = (
        costs["refund"]
        + costs["churn_orders"] * costs["margin"]
    )
    return numlate * cost_per_late_order


def BestPromise(zone, time_block, promises, costs=COSTS, seed=1, return_results=False):
    results = []
    best_promise = None
    best_profit = None

    for promise in promises:
        times = delivery_times(zone, time_block, promise, seed=seed)

        orders = len(times)
        late = int(np.sum(times > promise))

        profit = orders * costs["margin"] - LateCost(late, costs)
        results.append((promise, profit))

        if best_profit is None or profit > best_profit:
            best_profit = profit
            best_promise = promise

    if return_results:
        return best_promise, best_profit, results
    return best_promise, best_profit


zone = st.selectbox("Zone", ZONES)
time_block = st.selectbox("Time block", TIME_BLOCKS)

min_promise = st.number_input("Minimum promise", value=35, step=1)
max_promise = st.number_input("Maximum promise", value=65, step=1)
promise_step = st.number_input("Step", value=1, min_value=1, step=1)

margin = st.number_input(
    "Margin per order", value=float(COSTS["margin"]), step=0.01
)
churn_orders = st.number_input(
    "Future orders lost per late order",
    value=float(COSTS["churn_orders"]),
    step=0.01,
)
refund = st.number_input(
    "Refund per late order", value=float(COSTS["refund"]), step=0.01
)

if st.button("Calculate"):
    if min_promise >= max_promise:
        st.error("Minimum promise must be below maximum promise.")
    elif promise_step < 1:
        st.error("Step must be at least 1.")
    else:
        costs = {
            "refund": refund,
            "churn_orders": churn_orders,
            "margin": margin,
        }
        promises = list(range(min_promise, max_promise + 1, promise_step))
        best_promise, best_profit = BestPromise(
            zone, time_block, promises, costs=costs, seed=1
        )
        st.write(f"Recommended promise: {best_promise} minutes")
        st.write(f"Net profit: ${best_profit:,.2f}")