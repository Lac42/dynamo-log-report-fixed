Read the Apache-style access log at /app/access.log and write a JSON summary report to /app/report.json. Do not modify /app/access.log.

/app/report.json must be a single JSON object with exactly these three keys:
- "total_requests": integer — the number of non-empty lines in the log (one request per line).
- "unique_ips": integer — the number of distinct client IP addresses (the first whitespace-separated field of each line).
- "top_path": string — the request path (the target of the HTTP request line, e.g. "/index.html") that appears in the most requests. If two or more paths tie, use the one that appears first in the log.

Success criteria:
1. /app/report.json exists and is a single JSON object with exactly the keys "total_requests", "unique_ips", and "top_path".
2. "total_requests" equals the number of non-empty lines in /app/access.log.
3. "unique_ips" equals the number of distinct client IP addresses in the log.
4. "top_path" is the most-requested path (first-in-log on ties).

You have 120 seconds to complete this task. Do not cheat by using online solutions or hints specific to this task.
