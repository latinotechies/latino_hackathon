import json
import urllib
from bs4 import BeautifulSoup
import requests
from selenium import webdriver

BASE_URL = "http://12.218.239.82/i2/default.aspx?AspxAutoDetectCookieSupport=1"

def get_new_session_id():
    driver = webdriver.PhantomJS()
    driver.get(BASE_URL)
    cookies = driver.get_cookies()
    session_id_cookies = filter(lambda cookie: cookie['name'] == u'ASP.NET_SessionId', cookies)
    print session_id_cookies
    session_id_cookie = session_id_cookies[0]
    session_id = session_id_cookie['value']
    driver.close()
    return session_id


def encode_raw_form_data(form_data_raw):
    return dict(map(lambda s: s.split('='), filter(lambda _: len(_) > 0, form_data_raw.split('&'))))

def form_data_for_grantee_search():
    form_data_raw = """ScriptManager1=SearchFormEx1%24UpdatePanel%7CSearchFormEx1%24btnSearch&ScriptManager1_HiddenField=%3B%3BAjaxControlToolkit%2C%20Version%3D3.5.40412.0%2C%20Culture%3Dneutral%2C%20PublicKeyToken%3D28f01b0e84b6d53e%3Aen-US%3A1547e793-5b7e-48fe-8490-03a375b13a33%3Aeffe2a26%3B%3BAjaxControlToolkit%2C%20Version%3D3.5.40412.0%2C%20Culture%3Dneutral%2C%20PublicKeyToken%3D28f01b0e84b6d53e%3Aen-US%3A1547e793-5b7e-48fe-8490-03a375b13a33%3A475a4ef5%3A5546a2b%3A497ef277%3Aa43b07eb%3Ad2e10b12%3A37e2e5c9%3A5a682656%3A1d3ed089%3Af9029856%3Ad1a1d569%3Aaddc6819%3Ac7029a2%3Ae9e598a9%3B&__VIEWSTATE=&Navigator1%24SearchOptions1%24DocImagesCheck=on&SearchFormEx1%24ACSTextBox_LastName1=ih2&SearchFormEx1%24ACSDropDownList_DocumentType=-2&SearchFormEx1%24ACSTextBox_DateFrom=1%2F1%2F1985&SearchFormEx1%24ACSTextBox_DateTo=2%2F21%2F2015&ImageViewer1%24ScrollPos=&ImageViewer1%24ScrollPosChange=&ImageViewer1%24_imgContainerWidth=0&ImageViewer1%24_imgContainerHeight=0&ImageViewer1%24isImageViewerVisible=true&ImageViewer1%24hdnWidgetSize=&ImageViewer1%24DragResizeExtender_ClientState=&CertificateViewer1%24ScrollPos=&CertificateViewer1%24ScrollPosChange=&CertificateViewer1%24_imgContainerWidth=0&CertificateViewer1%24_imgContainerHeight=0&CertificateViewer1%24isImageViewerVisible=true&CertificateViewer1%24hdnWidgetSize=&CertificateViewer1%24DragResizeExtender_ClientState=&PTAXViewer1%24ScrollPos=&PTAXViewer1%24ScrollPosChange=&PTAXViewer1%24_imgContainerWidth=0&PTAXViewer1%24_imgContainerHeight=0&PTAXViewer1%24isImageViewerVisible=true&PTAXViewer1%24hdnWidgetSize=&PTAXViewer1%24DragResizeExtender_ClientState=&DocList1%24ctl09=&DocList1%24ctl11=&NameList1%24ScrollPos=&NameList1%24ScrollPosChange=True&NameList1%24_SortExpression=&NameList1%24ctl03=&NameList1%24ctl05=&DocDetails1%24PageSize=&DocDetails1%24PageIndex=&DocDetails1%24SortExpression=&BasketCtrl1%24ctl01=&BasketCtrl1%24ctl03=&OrderList1%24ctl01=&OrderList1%24ctl03=&__EVENTTARGET=&__EVENTARGUMENT=&__LASTFOCUS=&__ASYNCPOST=true&SearchFormEx1%24btnSearch=Search
    """
    form_data = encode_raw_form_data(form_data_raw)
    return form_data

def form_data_by_company_number(company_number):
    # This is the raw form data I captured from a single POST, when clicking on the Grantee results
    # for a particular company
    form_data_raw = """ScriptManager1=NameList1%24UpdatePanel%7CNameList1%24GridView_NameListGroup%24ctl12%24ctl03&ScriptManager1_HiddenField=%3B%3BAjaxControlToolkit%2C%20Version%3D3.5.40412.0%2C%20Culture%3Dneutral%2C%20PublicKeyToken%3D28f01b0e84b6d53e%3Aen-US%3A1547e793-5b7e-48fe-8490-03a375b13a33%3Aeffe2a26%3B%3BAjaxControlToolkit%2C%20Version%3D3.5.40412.0%2C%20Culture%3Dneutral%2C%20PublicKeyToken%3D28f01b0e84b6d53e%3Aen-US%3A1547e793-5b7e-48fe-8490-03a375b13a33%3A475a4ef5%3A5546a2b%3A497ef277%3Aa43b07eb%3Ad2e10b12%3A37e2e5c9%3A5a682656%3A1d3ed089%3Af9029856%3Ad1a1d569%3B%3BAjaxControlToolkit%2C%20Version%3D3.5.40412.0%2C%20Culture%3Dneutral%2C%20PublicKeyToken%3D28f01b0e84b6d53e%3Aen-US%3A1547e793-5b7e-48fe-8490-03a375b13a33%3Aaddc6819%3Ac7029a2%3Ae9e598a9%3B&__VIEWSTATE=&Navigator1%24SearchOptions1%24DocImagesCheck=on&SearchFormEx1%24ACSTextBox_LastName1=ih2&SearchFormEx1%24ACSDropDownList_DocumentType=-2&SearchFormEx1%24ACSTextBox_DateFrom=1%2F1%2F1985&SearchFormEx1%24ACSTextBox_DateTo=2%2F21%2F2015&ImageViewer1%24ScrollPos=&ImageViewer1%24ScrollPosChange=&ImageViewer1%24_imgContainerWidth=0&ImageViewer1%24_imgContainerHeight=0&ImageViewer1%24isImageViewerVisible=true&ImageViewer1%24hdnWidgetSize=&ImageViewer1%24DragResizeExtender_ClientState=&CertificateViewer1%24ScrollPos=&CertificateViewer1%24ScrollPosChange=&CertificateViewer1%24_imgContainerWidth=0&CertificateViewer1%24_imgContainerHeight=0&CertificateViewer1%24isImageViewerVisible=true&CertificateViewer1%24hdnWidgetSize=&CertificateViewer1%24DragResizeExtender_ClientState=&PTAXViewer1%24ScrollPos=&PTAXViewer1%24ScrollPosChange=&PTAXViewer1%24_imgContainerWidth=0&PTAXViewer1%24_imgContainerHeight=0&PTAXViewer1%24isImageViewerVisible=true&PTAXViewer1%24hdnWidgetSize=&PTAXViewer1%24DragResizeExtender_ClientState=&DocList1%24ctl09=&DocList1%24ctl11=&NameList1%24ScrollPos=&NameList1%24ScrollPosChange=True&NameList1%24_SortExpression=&NameList1%24ctl03=&NameList1%24ctl05=53&DocDetails1%24PageSize=&DocDetails1%24PageIndex=&DocDetails1%24SortExpression=&BasketCtrl1%24ctl01=&BasketCtrl1%24ctl03=&OrderList1%24ctl01=&OrderList1%24ctl03=&__EVENTTARGET=NameList1%24GridView_NameListGroup%24ctl12%24ctl03&__EVENTARGUMENT=&__LASTFOCUS=&__ASYNCPOST=true&"""
    form_data = encode_raw_form_data(form_data_raw)
    special_value = 'NameList1$GridView_NameListGroup$ctl%02d$ctl03' % company_number
    form_data['ScriptManager1'] = urllib.quote_plus('NameList1|' + special_value)
    form_data['__EVENTTARGET'] = urllib.quote_plus(special_value)
    return form_data

def get_response_by_post(form_data, session_id):
    # I captured these cookies from one request in Chrome; the session ID will probably need to be changed
    cookies_raw = "PopupImgWidth=800; PopupImgHeight=700; PopupImgTop=100; PopupImgLeft=100; AspxAutoDetectCookieSupport=1; ASP.NET_SessionId=%s; IsImageUndock=False; GroupListPageSize=50; PageSize=100" % session_id
    cookies = dict(map(lambda s: s.split('='), filter(lambda s: len(s) > 0, cookies_raw.split('; '))))
    r = requests.post(BASE_URL, data=json.dumps(form_data), cookies=cookies)
    return r.content

def get_pins_from_page_content(content):
    soup = BeautifulSoup(content)
    all_links = soup.find_all('a')
    pin_links = filter(lambda link: 'PIN' in (link.attrs.get('id') or ''), all_links)
    pins = map(lambda link: link.text, pin_links)
    return pins


def get_pins_by_company_number(company_number):
    html = get_results_by_company_number(company_number)
    pins = get_pins_from_page_content(html)
    return pins