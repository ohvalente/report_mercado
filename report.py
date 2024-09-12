import yfinance as yf 
import pandas as pd  
import matplotlib.pyplot as plt
import mplcyberpunk

from appscript import app, k, mactypes
# import mplcyberpunk

tickers = ["^BVSP", "^GSPC", "BRL=X"]
dados_mercado = yf.download(tickers, period = "6mo")

dados_mercado = dados_mercado["Adj Close"]

dados_mercado = dados_mercado.dropna()

dados_mercado.columns = ["DOLAR", "IBOVESPA", "S&P500"]

print(dados_mercado)

plt.style.use("cyberpunk")


# Gráfico IBOVESPA
plt.plot(dados_mercado["IBOVESPA"])
plt.title("IBOVESPA")
plt.show()
plt.savefig("ibovespa.png")

# Gráfico Dolar
plt.plot(dados_mercado["DOLAR"])
plt.title("DOLAR")
plt.show()
plt.savefig("dolar.png")

# Gráfico S&P500
plt.plot(dados_mercado["S&P500"])
plt.title("S&P500")
plt.show()
plt.savefig("s&p500.png")

retornos_diarios = dados_mercado.pct_change()

print(retornos_diarios)

retorno_dolar = retornos_diarios["DOLAR"].iloc[-1]
retorno_ibovespa = retornos_diarios["IBOVESPA"].iloc[-1]
retorno_sp = retornos_diarios["S&P500"].iloc[-1]

retorno_dolar = str(round(retorno_dolar * 100, 2)) + "%"

print(retorno_dolar)

retorno_ibovespa = str(round(retorno_ibovespa * 100, 2)) + "%"

print(retorno_ibovespa)

retorno_sp = str(round(retorno_sp * 100, 2)) + "%"

print(retorno_sp)

mail = app('Mail')

# Criar uma nova mensagem
nova_mensagem = mail.make(new=k.outgoing_message)

nova_mensagem.subject.set("Relatório de Mercado")

nova_mensagem.content.set(f'''Prezado diretor, segue o relatório de mercado:

* O Ibovespa teve o retorno de {retorno_ibovespa}.
* O Dólar teve o retorno de {retorno_dolar}.
* O S&P500 teve o retorno de {retorno_sp}.

Segue em anexo a peformance dos ativos nos últimos 6 meses.

Att,
Melhor estagiário do mundo


''')

nova_mensagem.sender.set("avalentetelles@icloud.com")

nova_mensagem.make(new=k.to_recipient, with_properties={k.address: "alevtelles@gmail.com"})

#O macbook tem o / certo, por isso nao precisa do r antes!

attachment = mactypes.File("/Users/valente/www/youtube/dolar.png") 
nova_mensagem.make(new=k.attachment, with_properties={k.file_name: attachment})
attachment = mactypes.File("/Users/valente/www/youtube/ibovespa.png")
nova_mensagem.make(new=k.attachment, with_properties={k.file_name: attachment})
attachment = mactypes.File("/Users/valente/www/youtube/sep500.png")
nova_mensagem.make(new=k.attachment, with_properties={k.file_name: attachment})

nova_mensagem.send()
