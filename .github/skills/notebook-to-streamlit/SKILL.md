---
name: notebook-to-streamlit
description: Port notebook functions into a self-contained Streamlit app without changing their logic.
---

# Notebook to Streamlit

Use this skill when turning functions from a Jupyter notebook into a Streamlit app.

## Rules

1. Port the notebook functions exactly as written. Do not rewrite or "improve" their logic.
2. The app must be self-contained in `app.py`. Copy the functions in; never import from the notebook.
3. Import `ZONES`, `TIME_BLOCKS`, `COSTS`, `PROMISE` and `delivery_times` from `starter`. Do not redefine them.
4. Build a fresh costs dict from the widgets using the same keys the functions read (`"refund"`, `"churn_orders"`, `"margin"`). Never modify the global `COSTS`.
5. Use a fixed seed so the same inputs always give the same result.
6. Build the promise list as `list(range(min_value, max_value + 1, step))`, since `range` excludes its end value.
7. Validate the range inputs before calculating: min must be below max and step must be at least 1. Show `st.error` otherwise.
8. Run the calculation only inside `if st.button(...)`.
9. Keep widget defaults, min values and steps the same numeric type (all ints or all floats).
10. Keep the app minimal. Build only what the spec lists, with no extra charts or state.