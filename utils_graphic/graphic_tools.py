import plotly.express as px

def plot_pie_chart(dataset, category_column, title=None):
    """
    Plots a pie chart using Plotly based on the given dataset and category column.

    Parameters:
        dataset (DataFrame): The dataset containing the churn data.
        category_column (str): The name of the column containing categorical churn data.

    Returns:
        None
    """
    if title is not None:
        graph_title = title
    else:
        graph_title= f'Churn Distribution ({category_column})'
    category_counts = dataset[category_column].value_counts()
    fig = px.pie(
        names=category_counts.index,
        values=category_counts.values,
        title=graph_title
    )
    fig.show()


def plot_scatter(dataset, x_column, y_column, hue_column, title):
    """
    Plots a scatter plot using Plotly based on the given dataset and columns.

    Parameters:
        dataset (DataFrame): The dataset containing the data.
        x_column (str): The name of the column for the x-axis.
        y_column (str): The name of the column for the y-axis.
        hue_column (str): The name of the column for the hue.
        title (str): The title of the scatter plot.

    Returns:
        None
    """
    fig = px.scatter(
        dataset,
        x=x_column,
        y=y_column,
        color=hue_column,
        title=title
    )
    fig.show()

