from src.tracing import create_traced_state, get_trace_summary
from src.performance import PerformanceMonitor
from src.errors import ErrorTracker
from src.feedback import FeedbackCollector


def test_tracing():
    """Test tracing functionality"""
    print("=" * 50)
    print("TESTING TRACING")
    print("=" * 50)
    
    state = create_traced_state("What is machine learning?")
    summary = get_trace_summary(state)
    
    print(f"Trace ID: {summary['trace_id'][:8]}...")
    print(f"Query: {summary['query']}")
    print(f"Execution time: {summary['execution_time']}s")
    print("✅ Tracing working\n")


def test_performance():
    """Test performance monitoring"""
    print("=" * 50)
    print("TESTING PERFORMANCE MONITOR")
    print("=" * 50)
    
    monitor = PerformanceMonitor()
    
    # Simulate 3 workflow runs
    for i in range(3):
        state = {
            "query": f"test query {i}",
            "execution_time": 3.0 + i,
            "step_count": 3,
            "token_estimate": 500,
            "cost_estimate": 0.001,
            "error": None,
            "trace_metadata": {"steps": []}
        }
        monitor.record_run(state)
    
    monitor.print_report()


def test_errors():
    """Test error tracking"""
    print("=" * 50)
    print("TESTING ERROR TRACKER")
    print("=" * 50)
    
    tracker = ErrorTracker()
    
    tracker.log_error("Connection timeout after 30 seconds")
    tracker.log_error("Rate limit exceeded, try again later")
    tracker.log_error("Token limit exceeded: 4096 max")
    tracker.log_error("Failed to parse JSON response")
    
    tracker.print_report()


def test_feedback():
    """Test feedback collection"""
    print("=" * 50)
    print("TESTING FEEDBACK COLLECTOR")
    print("=" * 50)
    
    collector = FeedbackCollector()
    
    collector.submit_feedback("trace-1", 5, "Excellent response!")
    collector.submit_feedback("trace-2", 4, "Good but could be better")
    collector.submit_feedback("trace-3", 3, "Average")
    collector.submit_feedback("trace-4", 2, "Not helpful")
    collector.submit_feedback("trace-5", 1, "Completely wrong")
    
    collector.print_report()


if __name__ == "__main__":
    print("\n🚀 LANGSMITH MONITORING SYSTEM TEST")
    print(f"👤 GitHub User: gvill0576")
    print(f"☁️  AWS Profile: default\n")
    
    test_tracing()
    test_performance()
    test_errors()
    test_feedback()
    
    print("\n✅ All monitoring systems tested successfully!")


