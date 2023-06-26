import requests,threading,os,json,urllib3
from nturl2path import url2pathname
from time import sleep
from bs4 import BeautifulSoup
from tqdm import tqdm

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)




# def progress():https://www.pixiv.net/artworks/109197185
#     os.path.getsize()
#     print()



urlinput = input("ID:")
# urlinput = '109061371'https://www.pixiv.net/artworks/107557220
# urlinput = '107557220'

print('正在解析')
headers= {
'Cookie':'first_visit_datetime_pc=2023-04-30+15%3A39%3A39; p_ab_id=2; p_ab_id_2=1; p_ab_d_id=1535423632; yuid_b=GJUQGCI; _gcl_au=1.1.507375444.1682836792; __utmz=235335808.1682836802.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); PHPSESSID=83267778_BDJCiIsEA6zSdxdRbwMtiMwL2TpJ1iMI; privacy_policy_notification=0; a_type=0; b_type=1; _ga_MZ1NL4PHH0=GS1.1.1682836816.1.1.1682836963.0.0.0; _fbp=fb.1.1682836994529.1279707460; login_ever=yes; __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=83267778=1^9=p_ab_id=2=1^10=p_ab_id_2=1=1^11=lang=zh=1; _ga_75BBYNYN9J=deleted; c_type=25; tag_view_ranking=0xsDLqCEW6~6qDO7xYZ-W~ybxe6VnJAU~LNEiPFsOr4~QL2G1t5h_V~qWFESUmfEs~8wnfTvwtRO~PGYs8AiIYn~Q-thmSPe-s~liM64qjhwQ~ETjPkL0e6r~6293srEnwa~q3eUobDMJW~z6i8Mevt17~L1pBzw5jVo~ZBoVMjk2oM~J9DAOECDjo~-qQoC8nrnQ~5VByp4g4N6~Lt-oEicbBr~Bo1xMRD4DT~kffGOewQdf~vTPS2OZsyP~RTJMXD26Ak~kGYw4gQ11Z~8PDkVxzRxX~xa5-CDAPro~6HUSQEiWHT~6a53MEkYjr~tzIoUMzCb7~x7Y9zfqbEJ~_EOd7bsGyl~ziiAzr_h04~hgM4Poq-Hh~0JvURp1dNS~pU_G10DOZG~9RiJSXmhLr~BSlt10mdnm~eInvgwdvwj~m7mtrljOwK~QKeXYK2oSR~OZbzcrhaSe~mzUOLCoPlB~HLWLeyYOUF~aKhT3n4RHZ~-oGijJmC5S~yFlkej57nn~Cy2fthLgAb~j4YdkYQPMe~uGQeWvelyQ~JEAYVsx1d9~k3AcsamkCa~D4hLr_YmAD~59dAqNEUGJ~fN7lpKqRmz~2OuHYpR2h4~1-NzAB_uw6~1F9SMtTyiX~abNIEh2zTB~hNe4Yo7r-q~YHg9nMmPjy~kngi6Qb_Ct~ds1AaoUmRE~FeEqwTOACZ~fTyU6WZAFB~9TIgdHUgpv~lPWnqPImPM~ash_mEA5x4~0jGVyl4Eky~qeU40VT-oU~jRiTFBcdb0~f4V1aCLsyM~NMgazSIQxY~TmShECZdw3~2vlJTO_OOx~0beaQMTutm~DEMRbxrB7a~AmSv_fD8MF~fQ7hBDQ-Oy~7kHMYSX6tr~2acjSVohem~lSaaPyMDfM~IYclAM59kT~yUv36CqH7A~YHRjLHL-7q~KVTNu2QtIE~laZrq0wMD9~t7dkWqcHOk~e9EFq9kkOU~CmMil8exOo~PVQkr3rLZQ~4G8hxJRSxE~oUdP9Ip2Au~T40wdiG5yy~dhD8snTBce~8gFm-X5GTV~NOuwwHwG6t~D0nMcn6oGk~XpZQOwdikq~ViIosn8nyc; privacy_policy_agreement=6; __utma=235335808.978885608.1682836802.1685891851.1687420685.9; __utmc=235335808; QSI_S_ZN_5hF4My7Ad6VNNAi=v:0:0; __utmb=235335808.2.10.1687420685; _ga_75BBYNYN9J=GS1.1.1687420688.6.1.1687420794.0.0.0; _ga=GA1.2.1663247289.1682836802; _gid=GA1.2.1053335222.1687420809',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
url = 'https://www.pixiv.net/ajax/illust/'+urlinput+'/pages?lang=zh'
strhtml = requests.get(url,headers=headers,verify=False)
res_json = json.loads(strhtml.text)

res_json = res_json['body']

headers = {
'Accept':'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
'Cookie':'first_visit_datetime_pc=2023-04-30+15%3A39%3A39; p_ab_id=2; p_ab_id_2=1; p_ab_d_id=1535423632; yuid_b=GJUQGCI; _gcl_au=1.1.507375444.1682836792; __utmz=235335808.1682836802.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); PHPSESSID=83267778_BDJCiIsEA6zSdxdRbwMtiMwL2TpJ1iMI; privacy_policy_notification=0; a_type=0; b_type=1; _ga_MZ1NL4PHH0=GS1.1.1682836816.1.1.1682836963.0.0.0; _fbp=fb.1.1682836994529.1279707460; login_ever=yes; __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=83267778=1^9=p_ab_id=2=1^10=p_ab_id_2=1=1^11=lang=zh=1; _ga_75BBYNYN9J=deleted; c_type=25; tag_view_ranking=0xsDLqCEW6~6qDO7xYZ-W~ybxe6VnJAU~LNEiPFsOr4~QL2G1t5h_V~qWFESUmfEs~8wnfTvwtRO~PGYs8AiIYn~Q-thmSPe-s~liM64qjhwQ~ETjPkL0e6r~6293srEnwa~q3eUobDMJW~z6i8Mevt17~L1pBzw5jVo~ZBoVMjk2oM~J9DAOECDjo~-qQoC8nrnQ~5VByp4g4N6~Lt-oEicbBr~Bo1xMRD4DT~kffGOewQdf~vTPS2OZsyP~RTJMXD26Ak~kGYw4gQ11Z~8PDkVxzRxX~xa5-CDAPro~6HUSQEiWHT~6a53MEkYjr~tzIoUMzCb7~x7Y9zfqbEJ~_EOd7bsGyl~ziiAzr_h04~hgM4Poq-Hh~0JvURp1dNS~pU_G10DOZG~9RiJSXmhLr~BSlt10mdnm~eInvgwdvwj~m7mtrljOwK~QKeXYK2oSR~OZbzcrhaSe~mzUOLCoPlB~HLWLeyYOUF~aKhT3n4RHZ~-oGijJmC5S~yFlkej57nn~Cy2fthLgAb~j4YdkYQPMe~uGQeWvelyQ~JEAYVsx1d9~k3AcsamkCa~D4hLr_YmAD~59dAqNEUGJ~fN7lpKqRmz~2OuHYpR2h4~1-NzAB_uw6~1F9SMtTyiX~abNIEh2zTB~hNe4Yo7r-q~YHg9nMmPjy~kngi6Qb_Ct~ds1AaoUmRE~FeEqwTOACZ~fTyU6WZAFB~9TIgdHUgpv~lPWnqPImPM~ash_mEA5x4~0jGVyl4Eky~qeU40VT-oU~jRiTFBcdb0~f4V1aCLsyM~NMgazSIQxY~TmShECZdw3~2vlJTO_OOx~0beaQMTutm~DEMRbxrB7a~AmSv_fD8MF~fQ7hBDQ-Oy~7kHMYSX6tr~2acjSVohem~lSaaPyMDfM~IYclAM59kT~yUv36CqH7A~YHRjLHL-7q~KVTNu2QtIE~laZrq0wMD9~t7dkWqcHOk~e9EFq9kkOU~CmMil8exOo~PVQkr3rLZQ~4G8hxJRSxE~oUdP9Ip2Au~T40wdiG5yy~dhD8snTBce~8gFm-X5GTV~NOuwwHwG6t~D0nMcn6oGk~XpZQOwdikq~ViIosn8nyc; privacy_policy_agreement=6; __utma=235335808.978885608.1682836802.1685891851.1687420685.9; __utmc=235335808; QSI_S_ZN_5hF4My7Ad6VNNAi=v:0:0; __utmb=235335808.2.10.1687420685; _ga_75BBYNYN9J=GS1.1.1687420688.6.1.1687420794.0.0.0; _ga=GA1.2.1663247289.1682836802; _gid=GA1.2.1053335222.1687420809',
'Referer':'https://www.pixiv.net/',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}
for res_json in res_json:

    res_json = res_json['urls']['original']
    res_name = res_json.split("/")[-1] # 文件名称

    res_rsize = requests.get(res_json,headers=headers,verify=False, stream=True)
    try:
           res_size = int(res_rsize.headers['content-length']) # 文件大小
    except:
            res_size = 0
    print(res_size)

    sleep(2.3)

    with open(res_name, 'wb') as file, tqdm(
        desc=res_name,
        total=res_size,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in res_rsize.iter_content(chunk_size=1024):
            size = file.write(data)
            bar.update(size)
