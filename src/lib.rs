use pyo3::prelude::*;

fn fibonacci(n: u64) -> u64 {
    if n <= 1 {
        return n;
    }
    fibonacci(n - 1) + fibonacci(n - 2)
}

#[pyfunction]
fn gil_freed_fibonacci(py: Python<'_>, n: u64) -> u64 {
    py.allow_threads(|| fibonacci(n))
}

#[pyfunction]
fn not_gil_freed_fibonacci(n: u64) -> u64 {
    fibonacci(n)
}

#[pymodule]
fn gil_free_python(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(gil_freed_fibonacci, m)?)?;
    m.add_function(wrap_pyfunction!(not_gil_freed_fibonacci, m)?)?;
    Ok(())
}
