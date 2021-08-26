import justpy as jp
from pandas.core.dtypes.common import classes
import pandas
from datetime import datetime

# Single line chart
chart_def = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Data analysis of course review rating'
    },
    subtitle: {
        text: 'Rating by day'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Time'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Rating star'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.y} star'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Rating Star',
        data: []
    }]
}
"""

# Multi line chart
chart_multi_def = """
{
    chart: {
        type: 'spline'
    },
    title: {
        text: 'Analysis rating by course by month'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 150,
        y: 100,
        floating: false,
        borderWidth: 1,
        backgroundColor: '#FFFFFF'
    },
    xAxis: {
        categories: [],
        plotBands: [{ // visualize the weekend
            from: 4.5,
            to: 6.5,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Rating star'
        }
    },
    tooltip: {
        shared: true,
        valueSuffix: ' star'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'John',
        data: [3, 4, 3, 5, 4, 10, 12]
    }, {
        name: 'Jane',
        data: [1, 3, 4, 3, 3, 5, 4]
    }]
}
"""

# Pie chart
chart_pie_def = """
{
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
    },
    title: {
        text: 'Course of python course'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            }
        }
    },
    series: [{
        name: 'Course',
        colorByPoint: true,
        data: [{
            name: 'Chrome',
            y: 61.41,
            sliced: true,
            selected: true
        }, {
            name: 'Internet Explorer',
            y: 11.84
        }, {
            name: 'Firefox',
            y: 10.85
        }, {
            name: 'Edge',
            y: 4.67
        }, {
            name: 'Safari',
            y: 4.18
        }, {
            name: 'Sogou Explorer',
            y: 1.64
        }, {
            name: 'Opera',
            y: 1.6
        }, {
            name: 'QQ',
            y: 1.2
        }, {
            name: 'Other',
            y: 2.61
        }]
    }]
}
"""

def getDataAnalysis():
    data = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])
    data["Day"] = data['Timestamp'].dt.date
    data["Week"] = data['Timestamp'].dt.strftime("%Y-%U")
    data["Month"] = data['Timestamp'].dt.strftime("%Y-%m")

    # Single line
    # data_average = data.groupby(["Day"]).mean()     # by Day
    # data_average = data.groupby(['Week']).mean()    # by Week
    # data_average = data.groupby(["Month"]).mean()   # by Month

    # Multi line
    # data_average = data.groupby(["Month", "Course Name"])["Rating"].mean().unstack()    # by Month by Course

    # Pie chart
    data_average = data.groupby(["Course Name"])["Rating"].count()

    return data_average

def makeApp():
    # create webpage object
    wp  = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="The graphs represent course review analysis")

    # Get data frame
    data = getDataAnalysis()

    # Add chart option
    # signal line chart
    # hc = jp.HighCharts(a=wp, options=chart_def)
    # hc.options.series[0].data = list(data["Rating"])

    # Multi line chart
    # hc = jp.HighCharts(a=wp, options=chart_multi_def)
    # hc_data = [{"name":v1, "data":[v2 for v2 in data[v1]]} for v1 in data.columns]
    # hc.options.series = hc_data

    # hc.options.xAxis.categories = list(data.index)

    # Pie chart
    hc = jp.HighCharts(a=wp, options=chart_pie_def)
    hc_data = [{"name": v1, "y": v2} for v1, v2 in zip(data.index, data)]
    hc.options.series[0].data = hc_data

    return wp

if __name__ == "__main__":
    jp.justpy(makeApp)

