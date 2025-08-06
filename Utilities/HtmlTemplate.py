def create_html_email(message, table_data, link_url, link_text):
    table_rows = "".join(
        f"<tr><td>{key.replace('_', ' ')}</td><td>{value}"
        for key, value in table_data
    )

    html_body = f"""
    <html>
    <head>
        <style>
            body {{ font-family: Calibri, sans-serif; }}
            .content {{ padding: 20px; }}
            .footer {{ background-color: #f9f9f9; padding: 10px; text-align: center; font-size: 12px; color: #888; }}
            table {{ width: 80%; border-collapse: collapse; margin-top: 20px; }}
            th, td {{ border: 1px solid #ccc; padding: 8px; text-align: left; }}
            a {{ display: inline; margin-top: 20px; color: #007BFF; text-decoration: none; }}
        </style>
    </head>
    <body>
        <div class="content">
            <p>{message}</p>
            <table>
                <tr><th>Field</th><th>Value</th></tr>
                {table_rows}
            </table>
            <p>Link: <a href="{link_url}">{link_text}</a></p>
            <p>Thanks & Regards,<br>Delta Capita</p>
        </div>
        <div class="footer">This is an automated message from your friendly Python bot.</div>
    </body>
    </html>
    """
    return html_body

 
