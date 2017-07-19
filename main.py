#twilio key
from twilioguy import TwilioGuy
from forecast import Forecast
import config as cfg

def send_message(text):
    #message = client.api.account.messages.create(to=text_number, from_=twilionumber, body=text)
    return

def main():
    #do stuff
    f = Forecast(cfg.dark_sky_key, "Chicago")
    
    message = ""
    
    avg_tmp = f.get_average_apparent_temp()
    
    if avg_tmp >= 80:
        message = message + "Tshirt/shorts "
    elif avg_tmp < 70:
        message = message + "Light jacket "
    elif avg_tmp < 55:
        message = message + "Pants + Heavy Jacket "
    elif avg_tmp < 32:
        message = message + "Gloves/Hat/Boots/Winter Jacket "
        
    if f.get_uvindex() > 4:
        message = message + "sunscreen/hat/shades "
        
    if f.get_precip_type() == "rain" and f.get_today_precip_chance() > .1:
        message = message + "umbrella "
    
    tg = TwilioGuy(cfg.twilio_account_sid, cfg.twilio_auth_token,
                    cfg.twilio_from_number, cfg.twilio_to_numbers)
    tg.send_message(message)
    
    
if __name__ == "__main__":
    main()