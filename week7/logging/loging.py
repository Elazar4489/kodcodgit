"""
תרגיל 1 – נכון / לא נכון
סמן V אם הטענה נכונה, X אם לא:
.1 לא נכון___ print ו-logging הם שקולים לחלוטין
.2 נכון___ DEBUG מתאים למידע מפורט בזמן פיתוח
.3 לא נכון___ מותר לכתוב סיסמה בלוג אם היא מוצפנת
.4 לא נכון___ WARNING אומר שהמערכת קרסה
.5 נכון___ FileHandler שומר לוגים לקובץ
6. stack trace גם כולל logger.exception ___נכון
.7 לא נכון___ כדאי להשתמש ברמת לוג אחת בלבד לפשטות
"""


"""
תרגיל 2 – התאמת רמת לוג
לכל תיאור, ציין את רמת הלוג המתאימה )ERROR / WARNING / INFO / DEBUG):
.1 משתמש התחבר בהצלחה: ___INFO
.2 קובץ קונפיגורציה לא נמצא: ___ERROR
.3 כניסה לפונקציה עם ערכי הפרמטרים: ___DEBUG
.4 מסד הנתונים לא זמין: ___ERROR
.5 מלאי מוצר נמוך מ5- יחידות: ___WARNING
.6 תהליך הזמנה הסתיים בהצלחה: ___INFO
"""

"""
תרגיל 3 – זיהוי בעיות
מצא את הבעיה בכל לוג ותקן:
# לוג א
logger.error('User logged in successfully')
הודעת הצלחה עם רמת error ואללה זה לא קשור
תיקון:
logger.info('User logged in successfully')

בעיה ותיקון: _______________________________________________
# לוג ב
logger.info('Login', email, password)
כתיבת סיסמה לקובץ לוג - לא תקין ולא בטוח
תיקון:
logger.info('Login', email, bool(password))

בעיה ותיקון: _______________________________________________
# לוג ג
print('ERROR: payment failed')
במקום לכתוב לקובץ לוג הוא מדפיס לטרמינל ולא שומר את התיעוד
תיקון:
logger.error('ERROR: payment failed')

בעיה ותיקון: ______________________________________________
"""


"""
תרגיל 4 – מה מייצג כל שדה?
הסבר מה מייצג כל שדה בפורמט הבא:
'%(asctime)s | %(levelname)s | %(name)s | %(message)s'

%(asctime)s = זמן 
%(levelname)s = רמת הלוג
%(name)s = שם (מוגדר או שם המודול)
%(message)s = הודעה המתארת את התיעוד

"""


"""
תרגיל 5 – השלם קוד
השלם כך שהקוד יריץ basicConfig עם INFO ויכתוב לוג אחד:
"""
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(name)s | %(message)s')
logger = logging.getLogger(__name__)
logger.info('Application started')


"""
רמה בינונית – יישום
תרגיל 6 – הפוך print ללוגים
שכתב את הקוד הבא כך שישתמש ב-logging במקום print:
"""

def process_payment(user_id, amount):
    loggerA=logging.getLogger("not print")
    logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(name)s | %(message)s')
    loggerA.info(f'Starting payment for user {user_id}')
    if amount <= 0:
        loggerA.error('ERROR: Invalid amount')
        return
    if amount > 10000:
        loggerA.warning('WARNING: Large transaction')
    loggerA.info(f'Payment of {amount} completed for user {user_id}')



process_payment("0001", 0)
process_payment("0002", 12000)
process_payment("0003", 1200)
process_payment("0004", 4000)
process_payment("0005", 1200000)


loggerB=logging.getLogger("payments")
formati=logging.Formatter('%(asctime)s | %(levelname)s | %(name)s | %(message)s')
file_handler=logging.FileHandler("app.log", encoding="utf-8")
file_handler.setFormatter(formati)

def add_3_loggers():
    loggerB.info("jdkjdijfkewjkdjewkdewkjdkewjf")
    








