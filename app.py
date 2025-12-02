{\rtf1\ansi\ansicpg936\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Italic;\f1\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red161\green0\blue48;\red251\green251\blue251;\red16\green16\blue16;
\red27\green81\blue131;\red208\green90\blue59;\red140\green126\blue203;\red167\green44\blue120;\red77\green50\blue164;
\red93\green138\blue149;\red48\green104\blue155;\red144\green40\blue3;}
{\*\expandedcolortbl;;\cssrgb\c70196\c0\c24706;\cssrgb\c98824\c98824\c98824;\cssrgb\c7843\c7843\c7843;
\cssrgb\c12549\c39608\c58431;\cssrgb\c85882\c43922\c29412;\cssrgb\c61961\c58039\c83529;\cssrgb\c72157\c26667\c54510;\cssrgb\c37647\c28627\c70196;
\cssrgb\c43529\c60784\c65098;\cssrgb\c23529\c48627\c67059;\cssrgb\c63922\c22353\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\i\fs24 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import
\f1\i0 \cf4 \strokec4  \cf5 \strokec5 streamlit\cf4 \strokec4  
\f0\i \cf2 \strokec2 as
\f1\i0 \cf4 \strokec4  \cf5 \strokec5 st\cf4 \cb1 \strokec4 \

\f0\i \cf2 \cb3 \strokec2 import
\f1\i0 \cf4 \strokec4  \cf5 \strokec5 google\cf4 \strokec4 .\cf5 \strokec5 generativeai\cf4 \strokec4  
\f0\i \cf2 \strokec2 as
\f1\i0 \cf4 \strokec4  \cf5 \strokec5 genai\cf4 \cb1 \strokec4 \

\f0\i \cf2 \cb3 \strokec2 import
\f1\i0 \cf4 \strokec4  \cf5 \strokec5 requests\cf4 \cb1 \strokec4 \

\f0\i \cf2 \cb3 \strokec2 import
\f1\i0 \cf4 \strokec4  \cf5 \strokec5 json\cf4 \cb1 \strokec4 \

\f0\i \cf2 \cb3 \strokec2 import
\f1\i0 \cf4 \strokec4  \cf5 \strokec5 re\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0

\f0\i \cf4 \cb3 # ==========================================
\f1\i0 \cb1 \

\f0\i \cb3 # \uc0\u39029 \u38754 \u37197 \u32622 
\f1\i0 \cb1 \

\f0\i \cb3 # ==========================================
\f1\i0 \cb1 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 st\cf4 \strokec4 .\cf6 \strokec6 set_page_config\cf4 \strokec4 (page_title=\cf7 \strokec7 "AI \uc0\u20869 \u23481 \u20013 \u21488  (\u35843 \u35797 \u29256 )"\cf4 \strokec4 , page_icon=\cf7 \strokec7 "\uc0\u55357 \u56350 "\cf4 \strokec4 , layout=\cf7 \strokec7 "wide"\cf4 \strokec4 )\cb1 \
\cf5 \cb3 \strokec5 st\cf4 \strokec4 .\cf6 \strokec6 title\cf4 \strokec4 (\cf7 \strokec7 "\uc0\u55357 \u56350  AI \u20869 \u23481 \u20013 \u21488  - \u25925 \u38556 \u25490 \u26597 \u27169 \u24335 "\cf4 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0

\f0\i \cf4 \cb3 # ==========================================
\f1\i0 \cb1 \

\f0\i \cb3 # \uc0\u20391 \u36793 \u26639 \u37197 \u32622 
\f1\i0 \cb1 \

\f0\i \cb3 # ==========================================
\f1\i0 \cb1 \
\pard\pardeftab720\partightenfactor0

\f0\i \cf2 \cb3 \strokec2 with
\f1\i0 \cf4 \strokec4  \cf5 \strokec5 st\cf4 \strokec4 .\cf5 \strokec5 sidebar\cf4 \strokec4 :\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf5 \strokec5 st\cf4 \strokec4 .\cf6 \strokec6 header\cf4 \strokec4 (\cf7 \strokec7 "\uc0\u9881 \u65039  \u25509 \u21475 \u37197 \u32622 "\cf4 \strokec4 )\cb1 \
\cb3     \cf5 \strokec5 GOOGLE_API_KEY\cf4 \strokec4  = \cf5 \strokec5 st\cf4 \strokec4 .\cf6 \strokec6 text_input\cf4 \strokec4 (\cf7 \strokec7 "Google API Key"\cf4 \strokec4 , type=\cf7 \strokec7 "password"\cf4 \strokec4 )\cb1 \
\cb3     \cb1 \
\cb3     \cf5 \strokec5 st\cf4 \strokec4 .\cf6 \strokec6 markdown\cf4 \strokec4 (\cf7 \strokec7 "---"\cf4 \strokec4 )\cb1 \
\cb3     \cf5 \strokec5 st\cf4 \strokec4 .\cf6 \strokec6 subheader\cf4 \strokec4 (\cf7 \strokec7 "\uc0\u39134 \u20070 \u37197 \u32622 "\cf4 \strokec4 )\cb1 \
\cb3     \cf5 \strokec5 FEISHU_APP_ID\cf4 \strokec4  = \cf5 \strokec5 st\cf4 \strokec4 .\cf6 \strokec6 text_input\cf4 \strokec4 (\cf7 \strokec7 "\uc0\u39134 \u20070  App ID (cli_\u24320 \u22836 )"\cf4 \strokec4 )\cb1 \
\cb3     \cf5 \strokec5 FEISHU_APP_SECRET\cf4 \strokec4  = \cf5 \strokec5 st\cf4 \strokec4 .\cf6 \strokec6 text_input\cf4 \strokec4 (\cf7 \strokec7 "\uc0\u39134 \u20070  App Secret"\cf4 \strokec4 , type=\cf7 \strokec7 "password"\cf4 \strokec4 )\cb1 \
\cb3     \cf5 \strokec5 FEISHU_APP_TOKEN\cf4 \strokec4  = \cf5 \strokec5 st\cf4 \strokec4 .\cf6 \strokec6 text_input\cf4 \strokec4 (\cf7 \strokec7 "Base Token (\uc0\u38142 \u25509 \u37324  app/ \u21518 \u38754 \u30340 )"\cf4 \strokec4 )\cb1 \
\cb3     \cf5 \strokec5 FEISHU_TABLE_ID\cf4 \strokec4  = \cf5 \strokec5 st\cf4 \strokec4 .\cf6 \strokec6 text_input\cf4 \strokec4 (\cf7 \strokec7 "Table ID (\uc0\u38142 \u25509 \u37324  tbl \u24320 \u22836 \u30340 )"\cf4 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0

\f0\i \cf4 \cb3 # ==========================================
\f1\i0 \cb1 \

\f0\i \cb3 # \uc0\u26680 \u24515 \u20989 \u25968  (\u24102 \u35814 \u32454 \u26085 \u24535 )
\f1\i0 \cb1 \

\f0\i \cb3 # ==========================================
\f1\i0 \cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf4 \strokec4  \cf6 \strokec6 get_feishu_token\cf4 \strokec4 ():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf5 \strokec5 st\cf4 \strokec4 .\cf6 \strokec6 info\cf4 \strokec4 (\cf7 \strokec7 "Step 2.1: \uc0\u27491 \u22312 \u23581 \u35797 \u33719 \u21462 \u39134 \u20070  Token..."\cf4 \strokec4 )\cb1 \
\cb3     \cf5 \strokec5 url\cf4 \strokec4  = \cf7 \strokec7 "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"\cf4 \cb1 \strokec4 \
\cb3     \cf5 \strokec5 headers\cf4 \strokec4  = \{\cf7 \strokec7 "Content-Type"\cf4 \strokec4 : \cf7 \strokec7 "application/json; charset=utf-8"\cf4 \strokec4 \}\cb1 \
\cb3     \cf5 \strokec5 payload\cf4 \strokec4  = \{\cb1 \
\cb3         \cf7 \strokec7 "app_id"\cf4 \strokec4 : \cf5 \strokec5 FEISHU_APP_ID\cf4 \strokec4 ,\cb1 \
\cb3         \cf7 \strokec7 "app_secret"\cf4 \strokec4 : \cf5 \strokec5 FEISHU_APP_SECRET\cf4 \cb1 \strokec4 \
\cb3     \}\cb1 \
\cb3     \cb1 \
\cb3     
\f0\i \cf2 \strokec2 try
\f1\i0 \cf4 \strokec4 :\cb1 \
\cb3         \cf5 \strokec5 resp\cf4 \strokec4  = \cf5 \strokec5 requests\cf4 \strokec4 .\cf6 \strokec6 post\cf4 \strokec4 (\cf5 \strokec5 url\cf4 \strokec4 , headers=\cf5 \strokec5 headers\cf4 \strokec4 , json=\cf5 \strokec5 payload\cf4 \strokec4 , timeout=\cf8 \strokec8 10\cf4 \strokec4 )\cb1 \
\cb3         \cf5 \strokec5 data\cf4 \strokec4  = \cf5 \strokec5 resp\cf4 \strokec4 .\cf6 \strokec6 json\cf4 \strokec4 ()\cb1 \
\cb3         \cb1 \
\cb3         
\f0\i # \uc0\u25171 \u21360 \u21407 \u22987 \u36820 \u22238 \u65292 \u26041 \u20415 \u25490 \u26597 
\f1\i0 \cb1 \
\cb3         \cf5 \strokec5 st\cf4 \strokec4 .\cf6 \strokec6 text\cf4 \strokec4 (\cf2 \strokec2 f\cf7 \strokec7 "\uc0\u39134 \u20070  Token \u25509 \u21475 \u36820 \u22238 : \cf6 \strokec6 \{\cf5 \strokec5 data\cf6 \strokec6 \}\cf7 \strokec7 "\cf4 \strokec4 )\cb1 \
\cb3         \cb1 \
\cb3         
\f0\i \cf2 \strokec2 if
\f1\i0 \cf4 \strokec4  \cf5 \strokec5 data\cf4 \strokec4 .\cf9 \strokec9 get\cf4 \strokec4 (\cf7 \strokec7 "code"\cf4 \strokec4 ) \cf2 \strokec2 ==\cf4 \strokec4  \cf8 \strokec8 0\cf4 \strokec4 :\cb1 \
\cb3             \cf5 \strokec5 st\cf4 \strokec4 .\cf6 \strokec6 success\cf4 \strokec4 (\cf7 \strokec7 "\uc0\u9989  \u39134 \u20070  Token \u33719 \u21462 \u25104 \u21151 "\cf4 \strokec4 )\cb1 \
\cb3             
\f0\i \cf2 \strokec2 return
\f1\i0 \cf4 \strokec4  \cf5 \strokec5 data\cf4 \strokec4 .\cf9 \strokec9 get\cf4 \strokec4 (\cf7 \strokec7 "tenant_access_token"\cf4 \strokec4 )\cb1 \
\cb3         
\f0\i \cf2 \strokec2 else
\f1\i0 \cf4 \strokec4 :\cb1 \
\cb3             \cf5 \strokec5 st\cf4 \strokec4 .\cf6 \strokec6 error\cf4 \strokec4 (\cf2 \strokec2 f\cf7 \strokec7 "\uc0\u10060  \u39134 \u20070 \u37492 \u26435 \u22833 \u36133 : \cf6 \strokec6 \{\cf5 \strokec5 data\cf4 \strokec4 .\cf9 \strokec9 get\cf4 \strokec4 (\cf7 \strokec7 'msg'\cf4 \strokec4 )\cf6 \strokec6 \}\cf7 \strokec7 "\cf4 \strokec4 )\cb1 \
\cb3             
\f0\i \cf2 \strokec2 return
\f1\i0 \cf4 \strokec4  \cf5 \strokec5 None\cf4 \cb1 \strokec4 \
\cb3     
\f0\i \cf2 \strokec2 except
\f1\i0 \cf4 \strokec4  \cf10 \strokec10 Exception\cf4 \strokec4  
\f0\i \cf2 \strokec2 as
\f1\i0 \cf4 \strokec4  \cf5 \strokec5 e\cf4 \strokec4 :\cb1 \
\cb3         \cf5 \strokec5 st\cf4 \strokec4 .\cf6 \strokec6 error\cf4 \strokec4 (\cf2 \strokec2 f\cf7 \strokec7 "\uc0\u10060  \u36830 \u25509 \u39134 \u20070 \u25509 \u21475 \u25253 \u38169 : \cf6 \strokec6 \{\cf5 \strokec5 e\cf6 \strokec6 \}\cf7 \strokec7 "\cf4 \strokec4 )\cb1 \
\cb3         
\f0\i \cf2 \strokec2 return
\f1\i0 \cf4 \strokec4  \cf5 \strokec5 None\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf4 \strokec4  \cf6 \strokec6 generate_content\cf4 \strokec4 (\cf6 \strokec6 topic\cf4 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf5 \strokec5 st\cf4 \strokec4 .\cf6 \strokec6 info\cf4 \strokec4 (\cf2 \strokec2 f\cf7 \strokec7 "Step 1: \uc0\u27491 \u22312 \u21457 \u36865 \u35831 \u27714 \u32473  Gemini (\u20027 \u39064 : \cf6 \strokec6 \{\cf4 \strokec4 topic\cf6 \strokec6 \}\cf7 \strokec7 )..."\cf4 \strokec4 )\cb1 \
\cb3     \cb1 \
\cb3     
\f0\i # \uc0\u26816 \u26597  Key
\f1\i0 \cb1 \
\cb3     
\f0\i \cf2 \strokec2 if
\f1\i0 \cf4 \strokec4  \cf2 \strokec2 not\cf4 \strokec4  \cf5 \strokec5 GOOGLE_API_KEY\cf4 \strokec4 :\cb1 \
\cb3         \cf5 \strokec5 st\cf4 \strokec4 .\cf6 \strokec6 error\cf4 \strokec4 (\cf7 \strokec7 "\uc0\u10060  \u38169 \u35823 : Google API Key \u20026 \u31354 \u65281 "\cf4 \strokec4 )\cb1 \
\cb3         
\f0\i \cf2 \strokec2 return
\f1\i0 \cf4 \strokec4  \cf5 \strokec5 None\cf4 \cb1 \strokec4 \
\
\cb3     
\f0\i \cf2 \strokec2 try
\f1\i0 \cf4 \strokec4 :\cb1 \
\cb3         \cf5 \strokec5 genai\cf4 \strokec4 .\cf6 \strokec6 configure\cf4 \strokec4 (api_key=\cf5 \strokec5 GOOGLE_API_KEY\cf4 \strokec4 )\cb1 \
\cb3         \cf5 \strokec5 model\cf4 \strokec4  = \cf5 \strokec5 genai\cf4 \strokec4 .\cf5 \strokec5 GenerativeModel\cf4 \strokec4 (\cf7 \strokec7 'gemini-1.5-pro'\cf4 \strokec4 ) 
\f0\i # \uc0\u36825 \u37324 \u30340 \u27169 \u22411 \u21517 \u30830 \u20445 \u27491 \u30830 
\f1\i0 \cb1 \
\cb3         \cb1 \
\cb3         \cf5 \strokec5 prompt\cf4 \strokec4  = \cf2 \strokec2 f\cf7 \strokec7 """\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7         \uc0\u20320 \u26159 \u19968 \u20010 \u36164 \u28145 \u30701 \u35270 \u39057 \u32534 \u23548 \u12290 \u35831 \u20998 \u26512 \u20027 \u39064 \u65306 \u12304 \cf6 \strokec6 \{\cf4 \strokec4 topic\cf6 \strokec6 \}\cf7 \strokec7 \uc0\u12305 \u12290 \cf4 \cb1 \strokec4 \
\cf7 \cb3 \strokec7         \uc0\u36755 \u20986 \u35201 \u27714 \u65306 \u21482 \u36755 \u20986 \u32431  JSON \u26684 \u24335 \u65292 \u19981 \u35201  Markdown \u26631 \u35760 \u12290 \cf4 \cb1 \strokec4 \
\cf7 \cb3 \strokec7         JSON \uc0\u23383 \u27573 \u65306 \cf4 \strokec4 \{\{\cf7 \strokec7 "topic": "\cf6 \strokec6 \{\cf4 \strokec4 topic\cf6 \strokec6 \}\cf7 \strokec7 ", "title": "\uc0\u26631 \u39064 ", "script": "\u33050 \u26412 \u20869 \u23481 "\cf4 \strokec4 \}\}\cb1 \
\cf7 \cb3 \strokec7         """\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3         \cb1 \
\cb3         
\f0\i # \uc0\u21457 \u36865 \u35831 \u27714 
\f1\i0 \cb1 \
\cb3         \cf5 \strokec5 response\cf4 \strokec4  = \cf5 \strokec5 model\cf4 \strokec4 .\cf6 \strokec6 generate_content\cf4 \strokec4 (\cf5 \strokec5 prompt\cf4 \strokec4 )\cb1 \
\cb3         \cb1 \
\cb3         
\f0\i # \uc0\u25171 \u21360  AI \u21407 \u22987 \u22238 \u22797 
\f1\i0 \cb1 \
\cb3         \cf5 \strokec5 st\cf4 \strokec4 .\cf6 \strokec6 write\cf4 \strokec4 (\cf7 \strokec7 "\uc0\u55357 \u56541  Gemini \u21407 \u22987 \u36820 \u22238 \u20869 \u23481 :"\cf4 \strokec4 )\cb1 \
\cb3         \cf5 \strokec5 st\cf4 \strokec4 .\cf6 \strokec6 code\cf4 \strokec4 (\cf5 \strokec5 response\cf4 \strokec4 .\cf9 \strokec9 text\cf4 \strokec4 )\cb1 \
\cb3         \cb1 \
\cb3         \cf5 \strokec5 text\cf4 \strokec4  = \cf5 \strokec5 response\cf4 \strokec4 .\cf9 \strokec9 text\cf4 \cb1 \strokec4 \
\cb3         \cf5 \strokec5 text\cf4 \strokec4  = \cf5 \strokec5 re\cf4 \strokec4 .\cf6 \strokec6 sub\cf4 \strokec4 (\cf2 \strokec2 r\cf7 \strokec7 '\cf11 \strokec11 ^```json\\s\cf12 \strokec12 *\cf7 \strokec7 '\cf4 \strokec4 , \cf7 \strokec7 ''\cf4 \strokec4 , \cf5 \strokec5 text\cf4 \strokec4 , flags=\cf5 \strokec5 re\cf4 \strokec4 .\cf5 \strokec5 MULTILINE\cf4 \strokec4 )\cb1 \
\cb3         \cf5 \strokec5 text\cf4 \strokec4  = \cf5 \strokec5 re\cf4 \strokec4 .\cf6 \strokec6 sub\cf4 \strokec4 (\cf2 \strokec2 r\cf7 \strokec7 '\cf11 \strokec11 ^```\\s\cf12 \strokec12 *\cf7 \strokec7 '\cf4 \strokec4 , \cf7 \strokec7 ''\cf4 \strokec4 , \cf5 \strokec5 text\cf4 \strokec4 , flags=\cf5 \strokec5 re\cf4 \strokec4 .\cf5 \strokec5 MULTILINE\cf4 \strokec4 )\cb1 \
\cb3         \cb1 \
\cb3         \cf5 \strokec5 data\cf4 \strokec4  = \cf5 \strokec5 json\cf4 \strokec4 .\cf6 \strokec6 loads\cf4 \strokec4 (\cf5 \strokec5 text\cf4 \strokec4 .\cf6 \strokec6 strip\cf4 \strokec4 ())\cb1 \
\cb3         \cf5 \strokec5 st\cf4 \strokec4 .\cf6 \strokec6 success\cf4 \strokec4 (\cf7 \strokec7 "\uc0\u9989  JSON \u35299 \u26512 \u25104 \u21151 "\cf4 \strokec4 )\cb1 \
\cb3         
\f0\i \cf2 \strokec2 return
\f1\i0 \cf4 \strokec4  \cf5 \strokec5 data\cf4 \cb1 \strokec4 \
\
\cb3     
\f0\i \cf2 \strokec2 except
\f1\i0 \cf4 \strokec4  \cf10 \strokec10 Exception\cf4 \strokec4  
\f0\i \cf2 \strokec2 as
\f1\i0 \cf4 \strokec4  \cf5 \strokec5 e\cf4 \strokec4 :\cb1 \
\cb3         \cf5 \strokec5 st\cf4 \strokec4 .\cf6 \strokec6 error\cf4 \strokec4 (\cf2 \strokec2 f\cf7 \strokec7 "\uc0\u10060  Gemini \u35831 \u27714 \u25110 \u35299 \u26512 \u22833 \u36133 : \cf6 \strokec6 \{\cf5 \strokec5 e\cf6 \strokec6 \}\cf7 \strokec7 "\cf4 \strokec4 )\cb1 \
\cb3         
\f0\i # \uc0\u26377 \u26102 \u20505 \u26159 \u22240 \u20026 \u23433 \u20840 \u35774 \u32622 \u23548 \u33268 \u36820 \u22238 \u20026 \u31354 \u65292 \u25171 \u21360 \u30475 \u30475 
\f1\i0 \cb1 \
\cb3         
\f0\i \cf2 \strokec2 if
\f1\i0 \cf4 \strokec4  \cf7 \strokec7 'response'\cf4 \strokec4  \cf2 \strokec2 in\cf4 \strokec4  \cf10 \strokec10 locals\cf4 \strokec4 () \cf2 \strokec2 and\cf4 \strokec4  \cf10 \strokec10 hasattr\cf4 \strokec4 (\cf5 \strokec5 response\cf4 \strokec4 , \cf7 \strokec7 'prompt_feedback'\cf4 \strokec4 ):\cb1 \
\cb3              \cf5 \strokec5 st\cf4 \strokec4 .\cf6 \strokec6 warning\cf4 \strokec4 (\cf2 \strokec2 f\cf7 \strokec7 "\uc0\u23433 \u20840 \u25318 \u25130 \u20449 \u24687 : \cf6 \strokec6 \{\cf5 \strokec5 response\cf4 \strokec4 .\cf9 \strokec9 prompt_feedback\cf6 \strokec6 \}\cf7 \strokec7 "\cf4 \strokec4 )\cb1 \
\cb3         
\f0\i \cf2 \strokec2 return
\f1\i0 \cf4 \strokec4  \cf5 \strokec5 None\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf4 \strokec4  \cf6 \strokec6 push_to_feishu\cf4 \strokec4 (\cf6 \strokec6 data\cf4 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf5 \strokec5 token\cf4 \strokec4  = \cf6 \strokec6 get_feishu_token\cf4 \strokec4 ()\cb1 \
\cb3     
\f0\i \cf2 \strokec2 if
\f1\i0 \cf4 \strokec4  \cf2 \strokec2 not\cf4 \strokec4  \cf5 \strokec5 token\cf4 \strokec4 : 
\f0\i \cf2 \strokec2 return
\f1\i0 \cf4 \strokec4  \cf5 \strokec5 False\cf4 \cb1 \strokec4 \
\
\cb3     \cf5 \strokec5 st\cf4 \strokec4 .\cf6 \strokec6 info\cf4 \strokec4 (\cf7 \strokec7 "Step 3: \uc0\u27491 \u22312 \u20889 \u20837 \u39134 \u20070 \u34920 \u26684 ..."\cf4 \strokec4 )\cb1 \
\cb3     \cf5 \strokec5 url\cf4 \strokec4  = \cf2 \strokec2 f\cf7 \strokec7 "https://open.feishu.cn/open-apis/bitable/v1/apps/\cf6 \strokec6 \{\cf5 \strokec5 FEISHU_APP_TOKEN\cf6 \strokec6 \}\cf7 \strokec7 /tables/\cf6 \strokec6 \{\cf5 \strokec5 FEISHU_TABLE_ID\cf6 \strokec6 \}\cf7 \strokec7 /records"\cf4 \cb1 \strokec4 \
\cb3     \cb1 \
\cb3     
\f0\i # \uc0\u26500 \u36896 \u26497 \u31616 \u25968 \u25454 \u20808 \u27979 \u35797 
\f1\i0 \cb1 \
\cb3     \cf5 \strokec5 fields\cf4 \strokec4  = \{\cb1 \
\cb3         \cf7 \strokec7 "\uc0\u20027 \u39064 "\cf4 \strokec4 : data.\cf9 \strokec9 get\cf4 \strokec4 (\cf7 \strokec7 "topic"\cf4 \strokec4 , \cf7 \strokec7 "\uc0\u26080 "\cf4 \strokec4 ),\cb1 \
\cb3         \cf7 \strokec7 "\uc0\u29190 \u27454 \u26631 \u39064 "\cf4 \strokec4 : data.\cf9 \strokec9 get\cf4 \strokec4 (\cf7 \strokec7 "title"\cf4 \strokec4 , \cf7 \strokec7 "\uc0\u26080 "\cf4 \strokec4 ), \cb1 \
\cb3         
\f0\i # \uc0\u27880 \u24847 \u65306 \u20808 \u21482 \u20256 \u20004 \u20010 \u23383 \u27573 \u65292 \u38450 \u27490 \u26159 \u22240 \u20026 \u23383 \u27573 \u21517 \u23545 \u19981 \u19978 \u23548 \u33268 \u30340 \u25253 \u38169 
\f1\i0 \cb1 \
\cb3     \}\cb1 \
\cb3     \cb1 \
\cb3     \cf5 \strokec5 st\cf4 \strokec4 .\cf6 \strokec6 write\cf4 \strokec4 (\cf7 \strokec7 "\uc0\u55357 \u56548  \u20934 \u22791 \u21457 \u36865 \u32473 \u39134 \u20070 \u30340 \u25968 \u25454  (Payload):"\cf4 \strokec4 )\cb1 \
\cb3     \cf5 \strokec5 st\cf4 \strokec4 .\cf6 \strokec6 json\cf4 \strokec4 (\cf5 \strokec5 fields\cf4 \strokec4 )\cb1 \
\
\cb3     \cf5 \strokec5 headers\cf4 \strokec4  = \{\cb1 \
\cb3         \cf7 \strokec7 "Authorization"\cf4 \strokec4 : \cf2 \strokec2 f\cf7 \strokec7 "Bearer \cf6 \strokec6 \{\cf5 \strokec5 token\cf6 \strokec6 \}\cf7 \strokec7 "\cf4 \strokec4 ,\cb1 \
\cb3         \cf7 \strokec7 "Content-Type"\cf4 \strokec4 : \cf7 \strokec7 "application/json; charset=utf-8"\cf4 \cb1 \strokec4 \
\cb3     \}\cb1 \
\cb3     \cb1 \
\cb3     
\f0\i \cf2 \strokec2 try
\f1\i0 \cf4 \strokec4 :\cb1 \
\cb3         \cf5 \strokec5 resp\cf4 \strokec4  = \cf5 \strokec5 requests\cf4 \strokec4 .\cf6 \strokec6 post\cf4 \strokec4 (\cf5 \strokec5 url\cf4 \strokec4 , headers=\cf5 \strokec5 headers\cf4 \strokec4 , json=\{\cf7 \strokec7 "fields"\cf4 \strokec4 : \cf5 \strokec5 fields\cf4 \strokec4 \}, timeout=\cf8 \strokec8 10\cf4 \strokec4 )\cb1 \
\cb3         \cf5 \strokec5 res_json\cf4 \strokec4  = \cf5 \strokec5 resp\cf4 \strokec4 .\cf6 \strokec6 json\cf4 \strokec4 ()\cb1 \
\cb3         \cb1 \
\cb3         \cf5 \strokec5 st\cf4 \strokec4 .\cf6 \strokec6 write\cf4 \strokec4 (\cf7 \strokec7 "\uc0\u55357 \u56549  \u39134 \u20070 \u20889 \u20837 \u25509 \u21475 \u36820 \u22238 :"\cf4 \strokec4 )\cb1 \
\cb3         \cf5 \strokec5 st\cf4 \strokec4 .\cf6 \strokec6 json\cf4 \strokec4 (\cf5 \strokec5 res_json\cf4 \strokec4 )\cb1 \
\cb3         \cb1 \
\cb3         
\f0\i \cf2 \strokec2 if
\f1\i0 \cf4 \strokec4  \cf5 \strokec5 res_json\cf4 \strokec4 .\cf9 \strokec9 get\cf4 \strokec4 (\cf7 \strokec7 "code"\cf4 \strokec4 ) \cf2 \strokec2 ==\cf4 \strokec4  \cf8 \strokec8 0\cf4 \strokec4 :\cb1 \
\cb3             
\f0\i \cf2 \strokec2 return
\f1\i0 \cf4 \strokec4  \cf5 \strokec5 True\cf4 \cb1 \strokec4 \
\cb3         
\f0\i \cf2 \strokec2 else
\f1\i0 \cf4 \strokec4 :\cb1 \
\cb3             \cf5 \strokec5 st\cf4 \strokec4 .\cf6 \strokec6 error\cf4 \strokec4 (\cf2 \strokec2 f\cf7 \strokec7 "\uc0\u10060  \u20889 \u20837 \u22833 \u36133 \u21407 \u22240 : \cf6 \strokec6 \{\cf5 \strokec5 res_json\cf4 \strokec4 .\cf9 \strokec9 get\cf4 \strokec4 (\cf7 \strokec7 'msg'\cf4 \strokec4 )\cf6 \strokec6 \}\cf7 \strokec7 "\cf4 \strokec4 )\cb1 \
\cb3             
\f0\i \cf2 \strokec2 return
\f1\i0 \cf4 \strokec4  \cf5 \strokec5 False\cf4 \cb1 \strokec4 \
\cb3     
\f0\i \cf2 \strokec2 except
\f1\i0 \cf4 \strokec4  \cf10 \strokec10 Exception\cf4 \strokec4  
\f0\i \cf2 \strokec2 as
\f1\i0 \cf4 \strokec4  \cf5 \strokec5 e\cf4 \strokec4 :\cb1 \
\cb3         \cf5 \strokec5 st\cf4 \strokec4 .\cf6 \strokec6 error\cf4 \strokec4 (\cf2 \strokec2 f\cf7 \strokec7 "\uc0\u10060  \u20889 \u20837 \u35831 \u27714 \u32593 \u32476 \u38169 \u35823 : \cf6 \strokec6 \{\cf5 \strokec5 e\cf6 \strokec6 \}\cf7 \strokec7 "\cf4 \strokec4 )\cb1 \
\cb3         
\f0\i \cf2 \strokec2 return
\f1\i0 \cf4 \strokec4  \cf5 \strokec5 False\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0

\f0\i \cf4 \cb3 # ==========================================
\f1\i0 \cb1 \

\f0\i \cb3 # \uc0\u20027 \u30028 \u38754 \u36923 \u36753 
\f1\i0 \cb1 \

\f0\i \cb3 # ==========================================
\f1\i0 \cb1 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 topic_input\cf4 \strokec4  = \cf5 \strokec5 st\cf4 \strokec4 .\cf6 \strokec6 text_input\cf4 \strokec4 (\cf7 \strokec7 "\uc0\u55357 \u56481  \u36755 \u20837 \u27979 \u35797 \u20027 \u39064 :"\cf4 \strokec4 )\cb1 \
\cf5 \cb3 \strokec5 run_btn\cf4 \strokec4  = \cf5 \strokec5 st\cf4 \strokec4 .\cf6 \strokec6 button\cf4 \strokec4 (\cf7 \strokec7 "\uc0\u55357 \u56960  \u24320 \u22987 \u25490 \u26597 "\cf4 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0

\f0\i \cf2 \cb3 \strokec2 if
\f1\i0 \cf4 \strokec4  \cf5 \strokec5 run_btn\cf4 \strokec4  \cf2 \strokec2 and\cf4 \strokec4  \cf5 \strokec5 topic_input\cf4 \strokec4 :\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf5 \strokec5 st\cf4 \strokec4 .\cf6 \strokec6 markdown\cf4 \strokec4 (\cf7 \strokec7 "---"\cf4 \strokec4 )\cb1 \
\cb3     \cf5 \strokec5 st\cf4 \strokec4 .\cf6 \strokec6 subheader\cf4 \strokec4 (\cf7 \strokec7 "\uc0\u55357 \u56522  \u25191 \u34892 \u26085 \u24535 "\cf4 \strokec4 )\cb1 \
\cb3     \cb1 \
\cb3     
\f0\i # 1. \uc0\u29983 \u25104 
\f1\i0 \cb1 \
\cb3     \cf5 \strokec5 data\cf4 \strokec4  = \cf6 \strokec6 generate_content\cf4 \strokec4 (\cf5 \strokec5 topic_input\cf4 \strokec4 )\cb1 \
\cb3     \cb1 \
\cb3     
\f0\i # 2. \uc0\u20889 \u20837 
\f1\i0 \cb1 \
\cb3     
\f0\i \cf2 \strokec2 if
\f1\i0 \cf4 \strokec4  \cf5 \strokec5 data\cf4 \strokec4 :\cb1 \
\cb3         \cf5 \strokec5 success\cf4 \strokec4  = \cf6 \strokec6 push_to_feishu\cf4 \strokec4 (\cf5 \strokec5 data\cf4 \strokec4 )\cb1 \
\cb3         
\f0\i \cf2 \strokec2 if
\f1\i0 \cf4 \strokec4  \cf5 \strokec5 success\cf4 \strokec4 :\cb1 \
\cb3             \cf5 \strokec5 st\cf4 \strokec4 .\cf6 \strokec6 balloons\cf4 \strokec4 ()\cb1 \
\cb3             \cf5 \strokec5 st\cf4 \strokec4 .\cf6 \strokec6 success\cf4 \strokec4 (\cf7 \strokec7 "\uc0\u55356 \u57225  \u24685 \u21916 \u65281 \u27969 \u31243 \u36305 \u36890 \u20102 \u65281 "\cf4 \strokec4 )\cb1 \
\cb3         
\f0\i \cf2 \strokec2 else
\f1\i0 \cf4 \strokec4 :\cb1 \
\cb3             \cf5 \strokec5 st\cf4 \strokec4 .\cf6 \strokec6 error\cf4 \strokec4 (\cf7 \strokec7 "\uc0\u55357 \u57003  \u27969 \u31243 \u20013 \u26029 \u65306 \u20889 \u20837 \u39134 \u20070 \u22833 \u36133 "\cf4 \strokec4 )\cb1 \
\cb3     
\f0\i \cf2 \strokec2 else
\f1\i0 \cf4 \strokec4 :\cb1 \
\cb3         \cf5 \strokec5 st\cf4 \strokec4 .\cf6 \strokec6 error\cf4 \strokec4 (\cf7 \strokec7 "\uc0\u55357 \u57003  \u27969 \u31243 \u20013 \u26029 \u65306 AI \u29983 \u25104 \u22833 \u36133 "\cf4 \strokec4 )\cb1 \
}