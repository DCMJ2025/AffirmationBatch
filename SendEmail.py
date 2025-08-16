import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from HtmlTemplate import create_html_email

def CreateEmailBodySendEmail(trade_data, token):
    subject=f"Affirmation Request || Trade ID: {trade_data.get("tradeid", "N/A")}"   
    message=f"""Hi Team,<br><br>This email request is for the purpose of affirming the trade economics to ensure both the parties are aware of the trade and main economic attributes.<br><br>Please review the detailed economics by clicking on below link."""
    # table_rows = "".join(
    #     f"<tr><td>{key.replace('_', ' ')}</td><td>{value}"
    #     for key, value in trade_data.items() if key not in ["tradeid", "Asset", "Product", "Productcategory"]
    #     )
    required_keys = ["tradeid", "Asset", "Product", "Productcategory"]
    key_labels = {
    "tradeid": "Trade Reference ID",
    "Asset": "Asset class",
    "Product": "Product",
    "Productcategory": "Product Category",
    }

    table_rows ="".join(
    f"<tr><td>{key_labels.get(key, key)}</td><td>{trade_data[key]}</td></tr>"
    for key in required_keys if key in trade_data
    )
    link=f"http://localhost:4200/tradedata?token={token}"
    send_email(
        subject=subject,
        to_email="mangesh.jambhulkar@deltacapita.com", 
        
        html_content_body= create_html_email(message, table_rows,link , "Click here to affirm the trade details")
    )
    print(f"Email sent with subject: {subject}")
    
def send_email(subject, to_email, html_content_body):
    sender_email='shardcdemo@gmail.com'
    msg = MIMEMultipart()
    msg['From'] = 'shardcdemo@gmail.com'
    msg['To'] = to_email
    msg['Subject'] = subject 
   
    msg.attach(MIMEText(html_content_body, 'html'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, 'rstk voic fesm yhnz')
            server.send_message(msg)
        print(f'Email sent successfully to {to_email}')
    except Exception as e:
        print(f'An error occurred while sending email: {e}')
