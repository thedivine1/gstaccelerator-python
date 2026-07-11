# GST Accelerator Python Client

Python client for the GST Accelerator API — India GST HSN/SAC lookup, GSTIN validation, and condition resolver.

## Installation

```bash
pip install gstaccelerator
```

## Quickstart

```python
from gstaccelerator import GSTAccelerator

gst = GSTAccelerator(api_key="your_api_key_here")
result = gst.hsn.get("84151010")
print(result)
```

## Method Reference

| Resource | Method | Description |
|---|---|---|
| `gst.hsn` | `get(code: str)` | HSN lookup |
| `gst.sac` | `get(code: str)` | SAC lookup |
| `gst` | `lookup(description: str, ...)` | Description search |
| `gst` | `autocomplete(query: str)` | Autocomplete |
| `gst` | `bulk(descriptions: list[str])` | Bulk lookup |
| `gst.gstin` | `validate(gstin: str)` | GSTIN validation |
| `gst.gstin` | `state(gstin: str)` | Get state info for GSTIN |
| `gst.gstin` | `pan(gstin: str)` | Get PAN info for GSTIN |
| `gst` | `health()` | Health check |
| `gst` | `meta()` | Meta data |

## Exception Handling

```python
from gstaccelerator import GSTAccelerator, RateLimitError, AuthenticationError

gst = GSTAccelerator(api_key="your_api_key_here")

try:
    result = gst.hsn.get("84151010")
except AuthenticationError as e:
    print(f"Auth failed: {e.message}")
except RateLimitError as e:
    print(f"Rate limited: {e.message}")
```

## Full Documentation

For full documentation, visit: https://gstaccelerator.in/docs
