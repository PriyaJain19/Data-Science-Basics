# ============================================================================
# PERSONAL EXPENSE TRACKER - Data Science Learning Project
# ============================================================================
# This project teaches data science basics through practical expense tracking
# 
# What you'll learn:
# Phase 1: Data Collection & Storage (Lists, Dicts)
# Phase 2: Data Cleaning & Preprocessing
# Phase 3: Basic Statistics & Analysis
# Phase 4: Grouping & Aggregation (Intro to Data Analysis)
# Phase 5: Visualization & Insights
# ============================================================================

from collections import defaultdict
from datetime import datetime, timedelta
import statistics

# ============================================================================
# PHASE 1: DATA COLLECTION & STORAGE
# ============================================================================
# In data science, everything starts with DATA
# We'll store expenses as dictionaries (records) in a list (dataset)

class ExpenseTracker:
    def __init__(self):
        # Our "dataset" - list of records (dictionaries)
        # Each record = one expense entry
        self.expenses = []
        
        # Sample data to work with
        self.load_sample_data()
    
    def load_sample_data(self):
        """Load sample expenses to practice analysis on"""
        sample_expenses = [
            {'date': '2024-01-01', 'category': 'Food', 'amount': 50, 'description': 'Lunch'},
            {'date': '2024-01-02', 'category': 'Transport', 'amount': 30, 'description': 'Auto'},
            {'date': '2024-01-03', 'category': 'Food', 'amount': 45, 'description': 'Dinner'},
            {'date': '2024-01-04', 'category': 'Entertainment', 'amount': 100, 'description': 'Movie'},
            {'date': '2024-01-05', 'category': 'Food', 'amount': 55, 'description': 'Groceries'},
            {'date': '2024-01-06', 'category': 'Utilities', 'amount': 200, 'description': 'Electricity'},
            {'date': '2024-01-07', 'category': 'Transport', 'amount': 25, 'description': 'Taxi'},
            {'date': '2024-01-08', 'category': 'Food', 'amount': 40, 'description': 'Lunch'},
            {'date': '2024-01-09', 'category': 'Entertainment', 'amount': 60, 'description': 'Concert'},
            {'date': '2024-01-10', 'category': 'Food', 'amount': 75, 'description': 'Restaurant'},
        ]
        self.expenses = sample_expenses
    
    def add_expense(self, date, category, amount, description):
        """
        Add a new expense to our dataset
        
        Data Science Concept: Recording observations/samples
        In ML/Data Science, each new data point is an observation
        """
        expense = {
            'date': date,
            'category': category,
            'amount': amount,
            'description': description
        }
        self.expenses.append(expense)
        print(f"✓ Added: {category} - ${amount}")
    
    # ========================================================================
    # PHASE 2: DATA CLEANING & PREPROCESSING
    # ========================================================================
    # Real data is messy! Data scientists spend 80% of time cleaning data
    
    def validate_expenses(self):
        """
        Data Quality Check
        Remove invalid/duplicate records
        """
        print("\n📊 DATA CLEANING:")
        print(f"  Initial records: {len(self.expenses)}")
        
        # Remove duplicates (same date, category, amount)
        seen = set()
        cleaned = []
        duplicates = 0
        
        for expense in self.expenses:
            # Create a tuple of key fields to check for duplicates
            key = (expense['date'], expense['category'], expense['amount'])
            
            if key not in seen:
                seen.add(key)
                cleaned.append(expense)
            else:
                duplicates += 1
        
        self.expenses = cleaned
        print(f"  Duplicates removed: {duplicates}")
        print(f"  Final clean records: {len(self.expenses)}")
    
    def remove_outliers(self, threshold_multiplier=3):
        """
        Identify unusual spending (outliers)
        
        Data Science Concept: Outlier Detection
        Outliers = data points that deviate significantly from others
        Common approach: values > mean + (std_dev × threshold_multiplier)
        """
        amounts = [e['amount'] for e in self.expenses]
        
        if len(amounts) < 2:
            return
        
        mean_amount = statistics.mean(amounts)
        std_dev = statistics.stdev(amounts)
        threshold = mean_amount + (std_dev * threshold_multiplier)
        
        outliers = [e for e in self.expenses if e['amount'] > threshold]
        
        print(f"\n⚠️  OUTLIER DETECTION:")
        print(f"  Mean spending: ${mean_amount:.2f}")
        print(f"  Std deviation: ${std_dev:.2f}")
        print(f"  Outlier threshold: ${threshold:.2f}")
        
        if outliers:
            print(f"  Found {len(outliers)} unusual expenses:")
            for expense in outliers:
                print(f"    • {expense['category']}: ${expense['amount']} ({expense['description']})")
        else:
            print("  No outliers detected")
    
    # ========================================================================
    # PHASE 3: BASIC STATISTICS & ANALYSIS
    # ========================================================================
    # Statistics are THE foundation of data science
    
    def calculate_statistics(self):
        """
        Compute basic statistics on spending
        
        Data Science Concepts:
        - Mean: Average (sum of all values / count)
        - Median: Middle value when sorted
        - Std Dev: How spread out the data is
        - Min/Max: Range of values
        """
        amounts = [e['amount'] for e in self.expenses]
        
        if not amounts:
            print("No expenses to analyze")
            return
        
        print("\n📈 STATISTICAL SUMMARY:")
        print(f"  Total expenses: {len(amounts)}")
        print(f"  Total spent: ${sum(amounts):.2f}")
        print(f"  Mean (avg): ${statistics.mean(amounts):.2f}")
        print(f"  Median: ${statistics.median(amounts):.2f}")
        print(f"  Min expense: ${min(amounts):.2f}")
        print(f"  Max expense: ${max(amounts):.2f}")
        
        if len(amounts) > 1:
            print(f"  Std deviation: ${statistics.stdev(amounts):.2f}")
            print(f"    (Higher = more variable spending)")
    
    # ========================================================================
    # PHASE 4: GROUPING & AGGREGATION
    # ========================================================================
    # Grouping = fundamental data analysis technique
    # You'll use this concept everywhere in data science!
    
    def analyze_by_category(self):
        """
        Group expenses by category and compute statistics
        
        Data Science Concept: Aggregation
        Grouping data by a column, then computing statistics = GROUP BY
        This is how you find patterns in data!
        """
        print("\n💰 ANALYSIS BY CATEGORY:")
        
        # Step 1: Group expenses by category
        # Using defaultdict (Python dict that groups things)
        categories = defaultdict(list)
        
        for expense in self.expenses:
            category = expense['category']
            amount = expense['amount']
            categories[category].append(amount)
        
        # Step 2: Calculate statistics for each group
        category_stats = []
        
        for category, amounts in sorted(categories.items()):
            stats = {
                'category': category,
                'count': len(amounts),
                'total': sum(amounts),
                'average': sum(amounts) / len(amounts),
                'min': min(amounts),
                'max': max(amounts)
            }
            category_stats.append(stats)
        
        # Step 3: Display results
        print(f"{'Category':<15} {'Count':<8} {'Total':<10} {'Avg':<10} {'Min-Max':<15}")
        print("-" * 58)
        
        for stats in category_stats:
            print(f"{stats['category']:<15} {stats['count']:<8} "
                  f"${stats['total']:<9.2f} ${stats['average']:<9.2f} "
                  f"${stats['min']:.0f}-${stats['max']:.0f}")
        
        return category_stats
    
    def analyze_by_date_range(self, days=7):
        """
        Analyze spending over time periods
        
        Data Science Concept: Time Series Analysis
        Looking at how data changes over time is crucial!
        """
        print(f"\n📅 LAST {days} DAYS ANALYSIS:")
        
        # Convert string dates to datetime for easier comparison
        # Note: In real projects, you'd use pandas for this (we'll avoid it here)
        daily_spending = defaultdict(float)
        
        for expense in self.expenses:
            date = expense['date']
            amount = expense['amount']
            daily_spending[date] += amount
        
        # Sort by date
        sorted_dates = sorted(daily_spending.items())
        
        print(f"{'Date':<15} {'Amount':<12} {'Trend'}")
        print("-" * 40)
        
        prev_amount = None
        for date, amount in sorted_dates:
            trend = ""
            if prev_amount is not None:
                change = amount - prev_amount
                trend = "↑" if change > 0 else "↓" if change < 0 else "→"
            
            print(f"{date:<15} ${amount:<11.2f} {trend}")
            prev_amount = amount
    
    def get_top_categories(self, n=3):
        """
        Find top N spending categories
        
        Data Science Concept: Ranking & Sorting
        Often you want to find the most important/biggest items
        """
        category_totals = defaultdict(float)
        
        for expense in self.expenses:
            category_totals[expense['category']] += expense['amount']
        
        # Sort by amount (descending) and get top N
        top_n = sorted(category_totals.items(), key=lambda x: x[1], reverse=True)[:n]
        
        print(f"\n🏆 TOP {n} SPENDING CATEGORIES:")
        for rank, (category, total) in enumerate(top_n, 1):
            percentage = (total / sum(category_totals.values())) * 100
            print(f"  {rank}. {category}: ${total:.2f} ({percentage:.1f}%)")
        
        return top_n
    
    # ========================================================================
    # PHASE 5: VISUALIZATION & INSIGHTS
    # ========================================================================
    # Visualizations help you "see" patterns humans can't see in numbers
    
    def print_spending_distribution(self):
        """
        Create a simple text-based visualization
        Shows distribution of spending amounts
        """
        print("\n📊 SPENDING DISTRIBUTION (using text):")
        
        amounts = sorted([e['amount'] for e in self.expenses])
        
        # Create buckets: 0-50, 50-100, 100-150, etc.
        buckets = defaultdict(int)
        
        for amount in amounts:
            bucket = (int(amount) // 50) * 50
            buckets[bucket] += 1
        
        print(f"{'Range':<15} {'Count':<8} {'Visualization'}")
        print("-" * 50)
        
        for bucket in sorted(buckets.keys()):
            count = buckets[bucket]
            bar = "█" * count  # Visual bar
            print(f"${bucket}-${bucket+50:<12} {count:<8} {bar}")
    
    def generate_insights(self):
        """
        Generate actionable insights from the data
        
        Data Science Concept: Business Intelligence
        Raw numbers → Insights → Actions
        """
        print("\n💡 KEY INSIGHTS:")
        
        if not self.expenses:
            print("  No data to analyze")
            return
        
        # Insight 1: Average daily spending
        total = sum(e['amount'] for e in self.expenses)
        avg_daily = total / len(self.expenses)
        print(f"  • Your average spending per transaction: ${avg_daily:.2f}")
        
        # Insight 2: Most expensive category
        categories = defaultdict(list)
        for expense in self.expenses:
            categories[expense['category']].append(expense['amount'])
        
        highest_cat = max(categories.items(), 
                         key=lambda x: sum(x[1]))
        print(f"  • Highest spending category: {highest_cat[0]} (${sum(highest_cat[1]):.2f})")
        
        # Insight 3: Spending trend
        amounts = [e['amount'] for e in self.expenses]
        if len(amounts) > 1:
            recent_avg = statistics.mean(amounts[-3:]) if len(amounts) >= 3 else amounts[-1]
            old_avg = statistics.mean(amounts[:3]) if len(amounts) >= 3 else amounts[0]
            
            trend = "increasing" if recent_avg > old_avg else "decreasing"
            print(f"  • Spending trend: {trend}")


# ============================================================================
# MAIN PROGRAM - Let's use our expense tracker!
# ============================================================================

def main():
    print("=" * 70)
    print("PERSONAL EXPENSE TRACKER - Data Science Learning Project")
    print("=" * 70)
    
    # Initialize tracker
    tracker = ExpenseTracker()
    
    print("\n✓ Loaded 10 sample expenses")
    
    # Phase 1: Explore the raw data
    print("\n" + "="*70)
    print("PHASE 1: RAW DATA (First 3 records)")
    print("="*70)
    for expense in tracker.expenses[:3]:
        print(f"  {expense}")
    
    tracker.add_expense('2024-01-15', 'Food', 65, 'Pizza with friends')
    
    # Phase 2: Clean the data
    print("\n" + "="*70)
    print("PHASE 2: DATA CLEANING & PREPROCESSING")
    print("="*70)
    tracker.validate_expenses()
    
    # Phase 3: Basic statistics
    print("\n" + "="*70)
    print("PHASE 3: DESCRIPTIVE STATISTICS")
    print("="*70)
    tracker.calculate_statistics()
    tracker.remove_outliers()
    
    # Phase 4: Grouping and aggregation
    print("\n" + "="*70)
    print("PHASE 4: GROUPING & AGGREGATION")
    print("="*70)
    tracker.analyze_by_category()
    tracker.get_top_categories(n=3)
    tracker.analyze_by_date_range(days=7)
    
    # Phase 5: Visualization and insights
    print("\n" + "="*70)
    print("PHASE 5: VISUALIZATION & INSIGHTS")
    print("="*70)
    tracker.print_spending_distribution()
    tracker.generate_insights()
    
    # Optional: Try adding your own expense
    print("\n" + "="*70)
    print("TRY IT YOURSELF")
    print("="*70)
    print("Uncomment the line below to add an expense:")
    
    # Then rerun the analysis to see how it changes!


if __name__ == "__main__":
    main()