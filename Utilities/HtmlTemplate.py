def create_html_email(subject, message, table_data, link_url, link_text):
    table_rows = "".join(
        f"<tr><td>{col1}</td><td>{col2}</td><td>{col3}</td></tr>"
        for col1, col2, col3 in table_data
    )

    html_body = f"""
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; }}
            .header {{ background-color: #f2f2f2; padding: 20px; text-align: center; font-size: 24px; font-weight: bold; }}
            .content {{ padding: 20px; }}
            .footer {{ background-color: #f9f9f9; padding: 10px; text-align: center; font-size: 12px; color: #888; }}
            table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
            th, td {{ border: 1px solid #ccc; padding: 8px; text-align: left; }}
            a {{ display: block; margin-top: 20px; color: #007BFF; text-decoration: none; }}
        </style>
    </head>
    <body>
        <div class="header">{subject}</div>
        <div class="content">
            <p>{message}</p>
            <table>
                <tr><th>Column 1</th><th>Column 2</th><th>Column 3</th></tr>
                {table_rows}
            </table>
            <a href="{link_url}">{link_text}</a>
        </div>
        <div class="footer">This is an automated message from your friendly Python bot.</div>
    </body>
    </html>
    """
    return html_body

# Example usage
email_html = create_html_email(
    subject="Weekly Update",
    message="Here are the latest stats from the system monitoring.",
    table_data=[("CPU Usage", "75%", "Stable"), ("Disk Space", "90%", "Critical"), ("Users Online", "254", "Healthy")],
    link_url="https://example.com/details",
    link_text="View Full Report"
)

print(email_html)