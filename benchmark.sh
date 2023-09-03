echo "sync benchmark result:"
wrk -t4 -c100 -d1m --timeout 30s http://localhost:8000/sync

echo "async benchmark result:"
wrk -t4 -c100 -d1m --timeout 30s http://localhost:8000/async
