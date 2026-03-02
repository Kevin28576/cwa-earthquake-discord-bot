import discord
from discord.ui import Button, View
from datetime import datetime

class sets:
    __slots__ = ["checkFile", "channels", "Tags", "APIToken", "token"]

    def __init__(self, token, APIToken=None, **kwargs):
        self.checkFile = kwargs.get("checkFile", "check.json")
        self.channels = list(map(int, kwargs.get("channels", "").split()))
        self.APIToken = APIToken
        self.token = token


def checkSos(ac):
    return {
        "0": "⚪",
        "1": "⚪",
        "2": "🟡",
        "3": "🟢",
        "4": "🟢",
        "5": "🔴",
        "6": "🟤",
        "7": "🟤",
        "8": "🟣",
        "9": "⚫"
    }[str(int(ac))] + " "

def checkSos_txt(ac_txt):
    return {
        "0": "無感",
        "1": "微震",
        "2": "輕震",
        "3": "弱震",
        "4": "中震",
        "5": "強震",
        "6": "烈震",
        "7": "劇震",
        "8": "劇震",
        "9": "劇震"
    }[str(int(ac_txt))] + ""

def checkSos_City(ac_City_txt):
    return {
        "最大震度1級地區": "<:3999number1:1170197041549410374> 級最大震度地區",
        "最大震度2級地區": "<:5675number2:1170197046456766495> 級最大震度地區",
        "最大震度3級地區": "<:7711number3:1170197050932084821> 級最大震度地區",
        "最大震度4級地區": "<:9315number4:1170197639355191357> 級最大震度地區",
        "最大震度5級地區": "<:2905number5:1170197039628431422> 級最大震度地區",
        "最大震度6級地區": "<:8959number6:1170197629200777298> 級最大震度地區",
        "最大震度7級地區": "<:7324number7:1170197049409540177> 級最大震度地區",
        "最大震度8級地區": "<:2133number8:1170197036667252746> 級最大震度地區",
        "最大震度9級地區": "<:8207number9:1170197054656626768> 級最大震度地區"
    }[str(ac_City_txt)] + ""

def checkSos_Send(ac_Send_txt):
    return {
        "無感": "<:announcement:1030688823841140786> **無感**:house_abandoned:報告!",
        "微震": "<:announcement:1030688823841140786> **微震**:house_abandoned:報告!",
        "輕震": "<:announcement:1030688823841140786> **輕震**:house_abandoned:報告!",
        "弱震": "<:announcement:1030688823841140786> **弱震**:house_abandoned:報告!",
        "中震": "<:announcement:1030688823841140786> **中震**:house_abandoned:報告! (<@&1170199357052698787>)",
        "強震": "<:2754danger:1170194558005563402> **強震**:house_abandoned:報告!! (<@&1170199357052698787>)",
        "烈震": "<:2754danger:1170194558005563402> <:2754danger:1170194558005563402> @everyone **烈震**:house_abandoned:報告!!!",
        "劇震": "<:2754danger:1170194558005563402> <:2754danger:1170194558005563402> @everyone **劇震**:house_abandoned:報告!!!"
    }[str(ac_Send_txt)] + ""

async def sosIn(channel, data, sets: sets):
    try:
        inp = data["records"]["Earthquake"][0]
        inpInfo = inp["EarthquakeInfo"]

        helpAwa = inp["Web"]  # 資料連結
        earthquakeNo = inp["EarthquakeNo"]  # 幾號地震
        if earthquakeNo == 112000:
            earthquakeNo_txt = "小區域有感地震"
        else:
            earthquakeNo_txt = f"第 {earthquakeNo} 號"

        location = inpInfo["Epicenter"]["Location"]  # 發生地點
        originTime = inpInfo["OriginTime"]  # 發生時間
        # 將原始時間字符串轉換為datetime對象
        original_time_str = originTime
        original_time = datetime.strptime(original_time_str, "%Y-%m-%d %H:%M:%S")

        # 將datetime對象格式化為所需的字符串格式
        formatted_time_str = original_time.strftime("<:pe_pink_arrow_right66:1170195482396598342> %Y年%m月%d日\n<:pe_pink_arrow_right66:1170195482396598342> %H時%M分%S秒")

        magnitudeType = inpInfo["EarthquakeMagnitude"]["MagnitudeType"]  # 規模單位
        magnitudeValue = inpInfo["EarthquakeMagnitude"]["MagnitudeValue"]  # 規模大小
        value = inpInfo["FocalDepth"]  # 地震深度
        EpicenterLongitude = inpInfo["Epicenter"]["EpicenterLongitude"]  # 發生地點-經度
        EpicenterLatitude = inpInfo["Epicenter"]["EpicenterLatitude"]  # 發生地點-緯度
        unit = '公里'  # 深度單位
        urlicon = inp["ReportImageURI"]  # 報告圖片
        cha = checkSos(magnitudeValue)
        cha_txt = checkSos_txt(magnitudeValue)
        embed = discord.Embed(title=data['records']['datasetDescription'],
                              description=inp['ReportContent'],
                              color=0xff0000, timestamp=datetime.utcnow())
        embed.set_author(
            name="台灣地震報告系統", icon_url='https://shop.jss.com.tw/data/goods/spec/opt/1582259793733168581.jpg')
        embed.set_image(url=f"{urlicon}")
        embed.add_field(name="<:divider:1170202031819063426><:divider:1170202031819063426><:divider:1170202031819063426><:divider:1170202031819063426><:divider:1170202031819063426><:divider:1170202031819063426>", value=f"　　　", inline=True)  # 分隔線
        embed.add_field(name="<:divider:1170202031819063426><:divider:1170202031819063426><:divider:1170202031819063426><:divider:1170202031819063426><:divider:1170202031819063426><:divider:1170202031819063426><:divider:1170202031819063426>", value=f"　　　", inline=True)  # 分隔線
        embed.add_field(name="<:divider:1170202031819063426><:divider:1170202031819063426><:divider:1170202031819063426><:divider:1170202031819063426><:divider:1170202031819063426><:divider:1170202031819063426>", value=f"　　　", inline=True)  # 分隔線
        embed.add_field(name="<:discordchannelfromvega:1031104455065731173> 編號", value=f"<:pe_pink_arrow_right66:1170195482396598342> {earthquakeNo_txt}", inline=True)  # 編號
        embed.add_field(name=f"<:2754danger:1170194558005563402> {magnitudeType}",
                        value=f"<:pe_pink_arrow_right66:1170195482396598342> {str(cha)}{magnitudeValue} ({cha_txt})", inline=True)  # 規模
        embed.add_field(name="<:dot:1026353526013706280> 震央位置", value=f"<:pe_pink_arrow_right66:1170195482396598342> {location}", inline=True)  # 震央位置
        embed.add_field(
            name="<:timer3:1170193105430007808> 發生時間", value=f"{formatted_time_str}", inline=True)  # 發生時間
        embed.add_field(name="<:Discord_partnerwaitapproval:1170194193109495819> 深度", value=f"<:pe_pink_arrow_right66:1170195482396598342> {value} {unit}", inline=True)  # 深度
        embed.add_field(name="<:4631_Location:1170201060300820500> 震央經緯度", value=f"<:pe_pink_arrow_right66:1170195482396598342> 經度: {EpicenterLongitude}\n<:pe_pink_arrow_right66:1170195482396598342> 緯度: {EpicenterLatitude}", inline=True)  # 震央經緯度
        embed.add_field(name="<:divider:1170202031819063426><:divider:1170202031819063426><:divider:1170202031819063426><:divider:1170202031819063426><:divider:1170202031819063426><:divider:1170202031819063426>", value=f"　　　", inline=True)  # 分隔線
        embed.add_field(name="<:divider:1170202031819063426><:divider:1170202031819063426><:divider:1170202031819063426><:divider:1170202031819063426><:divider:1170202031819063426><:divider:1170202031819063426><:divider:1170202031819063426>", value=f"　　　", inline=True)  # 分隔線
        embed.add_field(name="<:divider:1170202031819063426><:divider:1170202031819063426><:divider:1170202031819063426><:divider:1170202031819063426><:divider:1170202031819063426><:divider:1170202031819063426>", value=f"　　　", inline=True)  # 分隔線
        embed.set_footer(
            text=inp["ReportRemark"], icon_url='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/ROC_Central_Weather_Bureau.svg/1200px-ROC_Central_Weather_Bureau.svg.png')

        inp2 = inp["Intensity"]["ShakingArea"]
        for i in range(1, 10):
            for a in inp2:
                if str(i) in a["AreaDesc"]:
                    if "最大震度" in a["AreaDesc"]:
                        ai1 = a['AreaDesc']
                        ai2 = a['CountyName']
                        embed.add_field(name=f" {checkSos_City(ai1)} :",
                                        value=f"<:pe_pink_arrow_right66:1170195482396598342> {ai2}", inline=False)
                        
        goto_CWB_report = Button (label="中央氣象署報告", url=f"{helpAwa}", emoji="<:Discord_partnerwaitapproval:1170194193109495819>")
        view = View()
        view.add_item(goto_CWB_report)
        await channel.send(f"# {checkSos_Send(cha_txt)}", embed=embed, view=view)
    except Exception as err:
        print(err)