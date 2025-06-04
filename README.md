# Quantitative Financial Analysis Project

## Project Overview

This project focuses on analyzing financial and stock market data using Python libraries like pandas, matplotlib, and TA-Lib. It leverages datasets from Yahoo Finance (`yfinance`) to perform technical analysis, uncover trends, and extract actionable insights.

---

## Key Tasks Completed

### **1. Exploratory Data Analysis (EDA)**

#### **Descriptive Statistics**

- **Headline Length Analysis**: Calculated basic statistics such as average and maximum headline lengths to understand the distribution of textual data.
- **Article Count Per Publisher**: Visualized the number of articles published by each publisher to identify the most active contributors.
- **Publication Trends Over Time**: Analyzed temporal trends in article publication to identify patterns during key events.

#### **Text Analysis**

- **Sentiment Analysis**: Applied sentiment classification to group headlines into positive, negative, or neutral categories.
- **Keyword and Topic Extraction**: Identified frequent keywords and phrases (e.g., “FDA approval,” “price target”) for topic insights.

#### **Publisher Analysis**

- Highlighted publishers contributing the most news and explored their reporting styles (e.g., financial deep dives vs. breaking news).
  \_

---

### **2. Quantitative Analysis Using PyNance and TA-Lib**

#### **Data Preparation**

- Collected stock market data for seven distinct datasets via `yfinance`.
- Standardized datasets with essential columns like `Open`, `High`, `Low`, `Close`, and `Volume`.
- Organized all datasets into a single Jupyter Notebook for streamlined analysis.

#### **Technical Indicators**

Using **TA-Lib**, calculated:

- **Moving Averages (MA)**: 20-day and 50-day Simple Moving Averages to identify price trends.
- **Relative Strength Index (RSI)**: Measured momentum to detect overbought or oversold conditions.
- **MACD**: Analyzed short-term vs. long-term price movements to generate buy/sell signals.

#### **Visualization**

- Plotted closing prices with moving averages to highlight trend changes.
- Created RSI charts with overbought (70) and oversold (30) thresholds.
- Visualized MACD and signal lines to interpret momentum shifts.

### **3. Automated Analysis for Multiple Datasets**

- Unified analysis for all seven datasets in a single workflow.
- Used loops and dictionaries to automate indicator calculations and chart creation.
- Reduced manual effort by dynamically applying analysis to each dataset.

## Tools and Libraries Used

### **Python Libraries**

1. `pandas`: Data manipulation and cleaning.
2. `matplotlib`: Data visualization.
3. `TA-Lib`: Technical analysis indicators.
4. `yfinance`: Stock market data retrieval.

### **Data Sources**

- Historical stock data from Yahoo Finance via `yfinance`.

### **Development Platform**

- **Jupyter Notebook**: Centralized environment for coding, visualization, and reporting.

---

## How to Run the Notebook

1. **Install Required Libraries**:

   ```bash
   pip install pandas matplotlib yfinance TA-Lib
   ```

2. **Clone the Repository**:

```bash
git clone https://github.com/Sura-T/10-Academy.git
cd financial-analysis-project
```

3. **Launch Jupyter Notebook**:

```bash
jupyter notebook
```

4. **Execute the Notebook**:

- Open the notebook file.
- Run each cell sequentially to reproduce the analysis.

## Conclusion

This project demonstrates the power of combining EDA, technical analysis, and automation to extract valuable insights from financial data. By leveraging Python’s robust ecosystem, the analysis serves as a foundation for traders, investors, and financial analysts to make informed decisions.

