def compute_stats(numbers):
    stats = {
        "count": len(numbers),
        "sum": sum(numbers),
        "mean": sum(numbers) / len(numbers) if numbers else None,
        "min": min(numbers),
        "max": max(numbers),
        "median": sorted(numbers)[len(numbers) // 2] if len(numbers) % 2 == 1 else (
            sorted(numbers)[len(numbers) // 2 - 1] + sorted(numbers)[len(numbers) // 2]) / 2
    }
    return stats

def normalize(numbers):
    min_val, max_val = min(numbers), max(numbers)
    return [(n - min_val) / (max_val - min_val) if max_val != min_val else 0 for n in numbers]

def process_input(data):
    try:
        numbers = data.get("numbers", [])
        if not isinstance(numbers, list) or not all(isinstance(n, (int, float)) for n in numbers):
            return {"input": data, "valid": False, "error": "Invalid 'numbers': expected an array of numbers.", "code": "BAD_INPUT"}

        mode = data.get("mode", "basic")
        verbose = data.get("verbose", False)
        stats = compute_stats(numbers)
        result = {}

        if mode == "normalize":
            result = {"normalized": normalize(numbers), "method": "min-max"}
        elif mode not in ["basic", "normalize"]:
            return {"input": data, "valid": False, "error": f"Unsupported mode '{mode}'", "code": "BAD_MODE"}

        response = {
            "input": data,
            "valid": True,
            "mode": mode,
            "stats": stats
        }

        if result:
            response["result"] = result
        if verbose:
            response["explain"] = f"Computed count, sum, mean, min, max, median over {stats['count']} numbers."

        return response

    except Exception as e:
        return {"input": data, "valid": False, "error": str(e), "code": "UNEXPECTED_ERROR"}
