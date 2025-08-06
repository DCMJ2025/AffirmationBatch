import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from dataclasses import asdict
from Utilities.HtmlTemplate import create_html_email
from xmlParser import XmlParser
import logging

app_logger = logging.getLogger(__name__) 

sender_email='shardcdemo@gmail.com'

def send_email(subject, to_email, html_content_body):

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
        app_logger.info(f'Email sent successfully to {to_email}')
    except Exception as e:
        print(f'An error occurred while sending email: {e}')
        app_logger.error(f'An error occurred while sending email: {e}')

    
def extract_data(xml_path: str):
    parser = XmlParser()

    trade_data = parser.parse_xml(xml_path)

    if trade_data:
        table_data= []
        trade_details_dic= asdict(trade_data.trade_details)
        for key, value in trade_details_dic.items():
            if key == 'tradeid':
                continue
            table_data.append((key, value))
        #     party_dic= asdict(trade_data.party)
        # for key, value in party_dic.items():
        #     table_data.append((key, value))
            
                     
        subject=f"Affirmation Request || Trade ID: {trade_data.trade_details.Trade_Ref}"   
        message=f"""Hi Team,<br><br>This email request is for the purpose of affirming the trade economics to ensure both the parties are aware of the trade and main economic attributes.<br><br>Please review the detailed economics by clicking on below link."""                 
        
        send_email(
            subject=subject,
            to_email="sharvari.deshmukh@deltacapita.com", 
            html_content_body= create_html_email(message, table_data, "http://google.com" , "View in system")
        )

    else:
        print("Failed to parse XML")

