import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# ============================================================
# PAGE CONFIGURATION
# ============================================================
st.set_page_config(
    page_title="MAXX Byte | Robot Delivery Analytics",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS FOR BETTER CONTRAST
# ============================================================
st.markdown("""
<style>
    /* Main background */
    .stApp {
        background-color: #0e1117;
    }
    
    /* Metric cards */
    .stMetric {
        background-color: #1e1e2e;
        border-radius: 10px;
        padding: 10px;
        border-left: 4px solid #00ff88;
    }
    
    /* Metric labels */
    .stMetric label {
        color: #ffffff !important;
        font-weight: 600 !important;
    }
    
    /* Metric values */
    .stMetric .metric-value {
        color: #00ff88 !important;
        font-size: 32px !important;
    }
    
    /* Dataframe */
    .stDataFrame {
        background-color: #1e1e2e;
        border-radius: 10px;
    }
    
    /* Headers */
    h1, h2, h3 {
        color: #ffffff !important;
    }
    
    /* Sidebar */
    .css-1d391kg {
        background-color: #1a1a2e;
    }
    
    /* Sidebar text */
    .css-1d391kg .stMarkdown {
        color: #ffffff !important;
    }
    
    /* Buttons */
    .stButton button {
        background-color: #00ff88;
        color: #000000;
        font-weight: bold;
        border-radius: 20px;
    }
    
    /* Info boxes */
    .stAlert {
        background-color: #1e1e2e;
        color: #ffffff;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] button {
        color: #ffffff;
    }
    
    .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {
        color: #00ff88;
        border-bottom-color: #00ff88;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# DATABASE CONNECTION
# ============================================================
@st.cache_resource
def get_connection():
    try:
        return sqlite3.connect("robot_delivery.db")
    except Exception as e:
        st.error(f"Database connection error: {e}")
        return None

@st.cache_data(ttl=300)
def load_data(query):
    conn = get_connection()
    if conn:
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df
    return pd.DataFrame()

# ============================================================
# HEADER
# ============================================================
col1, col2 = st.columns([1, 4])
with col1:
    st.markdown("# 🤖")
with col2:
    st.markdown("# MAXX BYTE Robot Delivery Analytics")
    st.markdown("*Real-time delivery tracking and robot performance metrics*")

st.markdown("---")

# ============================================================
# SIDEBAR FILTERS
# ============================================================
with st.sidebar:
    st.markdown("## 🔍 Filters")
    st.markdown("---")
    
    # Date range filter
    date_range = st.selectbox(
        "Date Range",
        ["Last 7 Days", "Last 30 Days", "Last 90 Days", "All Time"],
        index=1
    )
    
    if date_range == "Last 7 Days":
        start_date = datetime.now() - timedelta(days=7)
        date_filter = f"timestamp >= '{start_date.strftime('%Y-%m-%d')}'"
    elif date_range == "Last 30 Days":
        start_date = datetime.now() - timedelta(days=30)
        date_filter = f"timestamp >= '{start_date.strftime('%Y-%m-%d')}'"
    elif date_range == "Last 90 Days":
        start_date = datetime.now() - timedelta(days=90)
        date_filter = f"timestamp >= '{start_date.strftime('%Y-%m-%d')}'"
    else:
        date_filter = "1=1"
    
    st.markdown("---")
    
    # Delivery type filter
    delivery_type = st.multiselect(
        "Delivery Type",
        ["robot", "human"],
        default=["robot", "human"]
    )
    
    type_filter = f"delivery_type IN ('{','.join(delivery_type)}')" if delivery_type else "1=1"
    
    st.markdown("---")
    
    # Profit range filter
    min_profit, max_profit = st.slider(
        "Profit Range ($)",
        min_value=-10,
        max_value=50,
        value=(-5, 30),
        step=5
    )
    
    profit_filter = f"profit BETWEEN {min_profit} AND {max_profit}"
    
    st.markdown("---")
    
    # Reset button
    if st.button("Reset Filters"):
        st.rerun()

# ============================================================
# BUILD WHERE CLAUSE
# ============================================================
where_clause = f"WHERE {date_filter} AND {type_filter} AND {profit_filter}"

# ============================================================
# METRICS ROW
# ============================================================
try:
    metrics_query = f"""
        SELECT 
            COUNT(*) as total_deliveries,
            ROUND(AVG(CASE WHEN delivery_type = 'robot' THEN time_taken END)/60, 1) as robot_avg_min,
            ROUND(AVG(CASE WHEN delivery_type = 'human' THEN time_taken END)/60, 1) as human_avg_min,
            ROUND(AVG(profit), 2) as avg_profit,
            ROUND(SUM(profit), 2) as total_profit,
            ROUND(100.0 * SUM(CASE WHEN time_taken <= 1200 THEN 1 ELSE 0 END) / COUNT(*), 1) as sla_pct
        FROM deliveries
        {where_clause}
    """
    
    metrics = load_data(metrics_query)
    
    if not metrics.empty:
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            st.metric(
                "Total Deliveries",
                f"{metrics['total_deliveries'].iloc[0]:,}",
                delta=None
            )
        
        with col2:
            st.metric(
                "Robot Avg Time",
                f"{metrics['robot_avg_min'].iloc[0]} min",
                delta="faster" if metrics['robot_avg_min'].iloc[0] < metrics['human_avg_min'].iloc[0] else "slower",
                delta_color="normal"
            )
        
        with col3:
            st.metric(
                "Human Avg Time",
                f"{metrics['human_avg_min'].iloc[0]} min",
                delta=None
            )
        
        with col4:
            sla_color = "normal" if metrics['sla_pct'].iloc[0] >= 95 else "inverse"
            st.metric(
                "SLA Compliance",
                f"{metrics['sla_pct'].iloc[0]}%",
                delta="Target: 95%",
                delta_color=sla_color
            )
        
        with col5:
            st.metric(
                "Total Profit",
                f"${metrics['total_profit'].iloc[0]:,.2f}",
                delta=None
            )
    else:
        st.warning("No data found for selected filters")
        
except Exception as e:
    st.error(f"Error loading metrics: {e}")

st.markdown("---")

# ============================================================
# CHARTS ROW
# ============================================================
col1, col2 = st.columns(2)

with col1:
    st.markdown("## 📈 SLA Compliance Trend")
    
    try:
        sla_query = f"""
            SELECT 
                DATE(timestamp) as date,
                ROUND(100.0 * SUM(CASE WHEN time_taken <= 1200 THEN 1 ELSE 0 END) / COUNT(*), 1) as sla_pct
            FROM deliveries
            {where_clause}
            GROUP BY DATE(timestamp)
            ORDER BY date DESC
            LIMIT 14
        """
        sla_data = load_data(sla_query)
        
        if not sla_data.empty:
            sla_data = sla_data.sort_values('date')
            
            fig = px.line(
                sla_data,
                x='date',
                y='sla_pct',
                title="SLA Compliance (Target: 95%)",
                labels={'date': 'Date', 'sla_pct': 'SLA %'}
            )
            
            fig.add_hline(y=95, line_dash="dash", line_color="red", annotation_text="Target")
            fig.update_layout(
                plot_bgcolor='#1e1e2e',
                paper_bgcolor='#1e1e2e',
                font_color='#ffffff',
                height=400
            )
            fig.update_traces(line_color='#00ff88', line_width=3)
            
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No SLA data available")
    except Exception as e:
        st.error(f"Error loading SLA chart: {e}")

with col2:
    st.markdown("## 🤖 Robot vs Human")
    
    try:
        compare_query = f"""
            SELECT 
                delivery_type,
                COUNT(*) as deliveries,
                ROUND(AVG(time_taken)/60, 1) as avg_minutes,
                ROUND(AVG(profit), 2) as avg_profit
            FROM deliveries
            {where_clause}
            GROUP BY delivery_type
        """
        compare_data = load_data(compare_query)
        
        if not compare_data.empty:
            fig = go.Figure()
            
            fig.add_trace(go.Bar(
                x=compare_data['delivery_type'],
                y=compare_data['avg_minutes'],
                name='Avg Minutes',
                marker_color='#00ff88',
                text=compare_data['avg_minutes'],
                textposition='auto'
            ))
            
            fig.add_trace(go.Bar(
                x=compare_data['delivery_type'],
                y=compare_data['avg_profit'],
                name='Avg Profit ($)',
                marker_color='#ff6b6b',
                text=compare_data['avg_profit'],
                textposition='auto'
            ))
            
            fig.update_layout(
                title="Robot vs Human Performance",
                barmode='group',
                plot_bgcolor='#1e1e2e',
                paper_bgcolor='#1e1e2e',
                font_color='#ffffff',
                height=400
            )
            
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No comparison data available")
    except Exception as e:
        st.error(f"Error loading comparison chart: {e}")

st.markdown("---")

# ============================================================
# DATA TABLE
# ============================================================
st.markdown("## 📋 Recent Deliveries")

try:
    data_query = f"""
        SELECT 
            delivery_id,
            timestamp,
            delivery_type,
            ROUND(time_taken/60, 1) as minutes,
            ROUND(revenue, 2) as revenue,
            ROUND(cost, 2) as cost,
            ROUND(profit, 2) as profit,
            CASE WHEN time_taken <= 1200 THEN '✅ On Time' ELSE '❌ Breached' END as sla_status
        FROM deliveries
        {where_clause}
        ORDER BY timestamp DESC
        LIMIT 100
    """
    
    df = load_data(data_query)
    
    if not df.empty:
        st.dataframe(
            df,
            use_container_width=True,
            column_config={
                "delivery_id": "Delivery ID",
                "timestamp": "Time",
                "delivery_type": "Type",
                "minutes": "Minutes",
                "revenue": st.column_config.NumberColumn("Revenue", format="$%.2f"),
                "cost": st.column_config.NumberColumn("Cost", format="$%.2f"),
                "profit": st.column_config.NumberColumn("Profit", format="$%.2f"),
                "sla_status": "SLA Status"
            }
        )
        
        # Download button
        csv = df.to_csv(index=False)
        st.download_button(
            label="📥 Download as CSV",
            data=csv,
            file_name=f"deliveries_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )
    else:
        st.info("No deliveries found for selected filters")
        
except Exception as e:
    st.error(f"Error loading data table: {e}")

st.markdown("---")
st.caption("MAXX Byte Robot Delivery Analytics | Data updates daily | SLA Target: 20 minutes (1200 seconds)")
