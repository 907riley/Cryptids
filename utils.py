def popup_html(row, df):
    name = df["Name"][row]
    description = df["Behaviour/Description"][row]
    location = df["Location"][row]

    left_col_color = "#19a7bd"
    right_col_color = "#f2f0d3"

    html = """<!DOCTYPE html>
    <html>
        <head>
            <h4 style="margin-bottom:10"; width="200px">{}</h4>""".format(name) + """
        </head>
        <table style="width:500px; font-size: px">
            <tr style="border: black 1px solid";>
                <td style="padding:2px; width: 100px;background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Description</span></td>
                <td style="padding:2px; width: 400px;background-color: """+ right_col_color +""";">{}</td>""".format(description) + """
            </tr>
            <tr style="border: black 1px solid";>
                <td style="padding:2px; width: 100px;background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Location</span></td>
                <td style="padding:2px; width: 400px;background-color: """+ right_col_color +""";">{}</td>""".format(location) + """
            </tr>
        </table>
    </html>
    """
    return html