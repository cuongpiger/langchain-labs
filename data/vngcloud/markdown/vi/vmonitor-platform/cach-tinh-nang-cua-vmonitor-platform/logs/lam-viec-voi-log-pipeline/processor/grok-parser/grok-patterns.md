# Grok Patterns

Bên dưới là danh sách các patterns mẫu mà chúng tôi gợi ý cho bạn: 

USERNAME \[a-zA-Z0-9._-]+ USER %{USERNAME} EMAILLOCALPART \[a-zA-Z0-9!#$%&'\*+-/=?^_`{|}~]{1,64}(?:\.[a-zA-Z0-9!#$%&'*+\-/=?^_`{|}\~]{1,62}){0,63} EMAILADDRESS %{EMAILLOCALPART}@%{HOSTNAME} INT (?:\[+-]?(?:\[0-9]+)) BASE10NUM (?\<!\[0-9.+-])(?>\[+-]?(?:(?:\[0-9]+(?:.\[0-9]+)?)|(?:.\[0-9]+))) NUMBER (?:%{BASE10NUM}) BASE16NUM (?\<!\[0-9A-Fa-f])(?:\[+-]?(?:0x)?(?:\[0-9A-Fa-f]+)) BASE16FLOAT \b(?\<!\[0-9A-Fa-f.])(?:\[+-]?(?:0x)?(?:(?:\[0-9A-Fa-f]+(?:.\[0-9A-Fa-f]\*)?)|(?:.\[0-9A-Fa-f]+)))\b

POSINT \b(?:\[1-9]\[0-9]_)\b NONNEGINT \b(?:\[0-9]+)\b WORD \b\w+\b NOTSPACE \S+ SPACE \s_ DATA ._? GREEDYDATA ._ QUOTEDSTRING (?>(?\<!\\)(?>"(?>\\.|\[^\\"]+)+"|""|(?>'(?>\\.|\[^\\']+)+')|''|(?>`(?>\\.|[^\\`]+)+\`)|\`\`)) UUID \[A-Fa-f0-9]{8}-(?:\[A-Fa-f0-9]{4}-){3}\[A-Fa-f0-9]{12}

\#URN, allowing use of RFC 2141 section 2.3 reserved characters

URN urn:\[0-9A-Za-z]\[0-9A-Za-z-]{0,31}:(?:%\[0-9a-fA-F]{2}|\[0-9A-Za-z()+,.:=@;$\_!\*'/?#-])+

\#Networking

MAC (?:%{CISCOMAC}|%{WINDOWSMAC}|%{COMMONMAC}) CISCOMAC (?:(?:\[A-Fa-f0-9]{4}.){2}\[A-Fa-f0-9]{4}) WINDOWSMAC (?:(?:\[A-Fa-f0-9]{2}-){5}\[A-Fa-f0-9]{2}) COMMONMAC (?:(?:\[A-Fa-f0-9]{2}:){5}\[A-Fa-f0-9]{2}) IPV6 (((\[0-9A-Fa-f]{1,4}:){7}(\[0-9A-Fa-f]{1,4}|:))|((\[0-9A-Fa-f]{1,4}:){6}(:\[0-9A-Fa-f]{1,4}|((25\[0-5]|2\[0-4]\d|1\d\d|\[1-9]?\d)(.(25\[0-5]|2\[0-4]\d|1\d\d|\[1-9]?\d)){3})|:))|((\[0-9A-Fa-f]{1,4}:){5}(((:\[0-9A-Fa-f]{1,4}){1,2})|:((25\[0-5]|2\[0-4]\d|1\d\d|\[1-9]?\d)(.(25\[0-5]|2\[0-4]\d|1\d\d|\[1-9]?\d)){3})|:))|((\[0-9A-Fa-f]{1,4}:){4}(((:\[0-9A-Fa-f]{1,4}){1,3})|((:\[0-9A-Fa-f]{1,4})?:((25\[0-5]|2\[0-4]\d|1\d\d|\[1-9]?\d)(.(25\[0-5]|2\[0-4]\d|1\d\d|\[1-9]?\d)){3}))|:))|((\[0-9A-Fa-f]{1,4}:){3}(((:\[0-9A-Fa-f]{1,4}){1,4})|((:\[0-9A-Fa-f]{1,4}){0,2}:((25\[0-5]|2\[0-4]\d|1\d\d|\[1-9]?\d)(.(25\[0-5]|2\[0-4]\d|1\d\d|\[1-9]?\d)){3}))|:))|((\[0-9A-Fa-f]{1,4}:){2}(((:\[0-9A-Fa-f]{1,4}){1,5})|((:\[0-9A-Fa-f]{1,4}){0,3}:((25\[0-5]|2\[0-4]\d|1\d\d|\[1-9]?\d)(.(25\[0-5]|2\[0-4]\d|1\d\d|\[1-9]?\d)){3}))|:))|((\[0-9A-Fa-f]{1,4}:){1}(((:\[0-9A-Fa-f]{1,4}){1,6})|((:\[0-9A-Fa-f]{1,4}){0,4}:((25\[0-5]|2\[0-4]\d|1\d\d|\[1-9]?\d)(.(25\[0-5]|2\[0-4]\d|1\d\d|\[1-9]?\d)){3}))|:))|(:(((:\[0-9A-Fa-f]{1,4}){1,7})|((:\[0-9A-Fa-f]{1,4}){0,5}:((25\[0-5]|2\[0-4]\d|1\d\d|\[1-9]?\d)(.(25\[0-5]|2\[0-4]\d|1\d\d|\[1-9]?\d)){3}))|:)))(%.+)? IPV4 (?\<!\[0-9])(?:(?:\[0-1]?\[0-9]{1,2}|2\[0-4]\[0-9]|25\[0-5])...)(?!\[0-9]) IP (?:%{IPV6}|%{IPV4}) HOSTNAME \b(?:\[0-9A-Za-z]\[0-9A-Za-z-]{0,62})(?:.(?:\[0-9A-Za-z]\[0-9A-Za-z-]{0,62}))\*(.?|\b) IPORHOST (?:%{IP}|%{HOSTNAME}) HOSTPORT %{IPORHOST}:%{POSINT}

\#paths (only absolute paths are matched)

PATH (?:%{UNIXPATH}|%{WINPATH}) UNIXPATH (/\[\[\[:alnum:]]\_%!$@:.,+\~-]_)+ TTY (?:/dev/(pts|tty(\[pq])?)(\w+)?/?(?:\[0-9]+)) WINPATH (?>\[A-Za-z]+:|\\)(?:\\\[^\\?_]\*)+ URIPROTO A-Za-z+ URIHOST %{IPORHOST}(?::%{POSINT})?

\#uripath comes loosely from RFC1738, but mostly from what Firefox doesn't turn into %XX

URIPATH (?:/\[A-Za-z0-9$.+!_'(){},\~:;=@#%&\_-]_)+ URIQUERY \[A-Za-z0-9$.+!_'|(){},\~@#%&/=:;\_?-\[]<>]_

\#deprecated (kept due compatibility):

URIPARAM ?%{URIQUERY} URIPATHPARAM %{URIPATH}(?:?%{URIQUERY})? URI %{URIPROTO}://(?:%{USER}(?::\[^@]\*)?@)?(?:%{URIHOST})?(?:%{URIPATH}(?:?%{URIQUERY})?)?

\#Months: January, Feb, 3, 03, 12, December

MONTH \b(?:\[Jj]an(?:uary|uar)?|\[Ff]eb(?:ruary|ruar)?|Mm?r(?:ch|z)?|\[Aa]pr(?:il)?|\[Mm]a(?:y|i)?|\[Jj]un(?:e|i)?|\[Jj]ul(?:y|i)?|\[Aa]ug(?:ust)?|\[Ss]ep(?:tember)?|Oo?t(?:ober)?|\[Nn]ov(?:ember)?|\[Dd]e(?:c|z)(?:ember)?)\b MONTHNUM (?:0?\[1-9]|1\[0-2]) MONTHNUM2 (?:0\[1-9]|1\[0-2]) MONTHDAY (?:(?:0\[1-9])|(?:\[12]\[0-9])|(?:3\[01])|\[1-9])

\#Days: Monday, Tue, Thu, etc...

DAY (?:Mon(?:day)?|Tue(?:sday)?|Wed(?:nesday)?|Thu(?:rsday)?|Fri(?:day)?|Sat(?:urday)?|Sun(?:day)?)

\#Years?

YEAR (?>\d\d){1,2} HOUR (?:2\[0123]|\[01]?\[0-9]) MINUTE (?:\[0-5]\[0-9])

\#'60' is a leap second in most time standards and thus is valid.

SECOND (?:(?:\[0-5]?\[0-9]|60)(?:\[:.,]\[0-9]+)?) TIME (?!<\[0-9])%{HOUR}:%{MINUTE}(?::%{SECOND})(?!\[0-9])

\#datestamp is YYYY/MM/DD-HH:MM:SS.UUUU (or something like it)

DATE\_US %{MONTHNUM}\[/-]%{MONTHDAY}\[/-]%{YEAR} DATE\_EU %{MONTHDAY}\[./-]%{MONTHNUM}\[./-]%{YEAR} ISO8601\_TIMEZONE (?:Z|\[+-]%{HOUR}(?::?%{MINUTE})) ISO8601\_SECOND %{SECOND} TIMESTAMP\_ISO8601 %{YEAR}-%{MONTHNUM}-%{MONTHDAY}\[T ]%{HOUR}:?%{MINUTE}(?::?%{SECOND})?%{ISO8601\_TIMEZONE}? DATE %{DATE\_US}|%{DATE\_EU} DATESTAMP %{DATE}\[- ]%{TIME} TZ (?:\[APMCE]\[SD]T|UTC) DATESTAMP\_RFC822 %{DAY} %{MONTH} %{MONTHDAY} %{YEAR} %{TIME} %{TZ} DATESTAMP\_RFC2822 %{DAY}, %{MONTHDAY} %{MONTH} %{YEAR} %{TIME} %{ISO8601\_TIMEZONE} DATESTAMP\_OTHER %{DAY} %{MONTH} %{MONTHDAY} %{TIME} %{TZ} %{YEAR} DATESTAMP\_EVENTLOG %{YEAR}%{MONTHNUM2}%{MONTHDAY}%{HOUR}%{MINUTE}%{SECOND}

\#Syslog Dates: Month Day HH:MM:SS

SYSLOGTIMESTAMP %{MONTH} +%{MONTHDAY} %{TIME} PROG \[\x21-\x5a\x5c\x5e-\x7e]+ SYSLOGPROG %{PROG:\[process]\[name]}(?:\[%{POSINT:\[process]\[pid]:int}])? SYSLOGHOST %{IPORHOST} SYSLOGFACILITY <%{NONNEGINT:\[log]\[syslog]\[facility]\[code]:int}.%{NONNEGINT:\[log]\[syslog]\[priority]:int}> HTTPDATE %{MONTHDAY}/%{MONTH}/%{YEAR}:%{TIME} %{INT}

\#Shortcuts

QS %{QUOTEDSTRING}

\#Log formats

SYSLOGBASE %{SYSLOGTIMESTAMP:timestamp} (?:%{SYSLOGFACILITY} )?%{SYSLOGHOST:\[host]\[hostname]} %{SYSLOGPROG}:

\#Log Levels

LOGLEVEL (\[Aa]lert|ALERT|\[Tt]race|TRACE|\[Dd]ebug|DEBUG|\[Nn]otice|NOTICE|\[Ii]nfo?(?:rmation)?|INFO?(?:RMATION)?|\[Ww]arn?(?:ing)?|WARN?(?:ING)?|\[Ee]rr?(?:or)?|ERR?(?:OR)?|\[Cc]rit?(?:ical)?|CRIT?(?:ICAL)?|\[Ff]atal|FATAL|\[Ss]evere|SEVERE|EMERG(?:ENCY)?|\[Ee]merg(?:ency)?
