Summary:	The SquirrelMail, a WebMail package
Summary(pl):	Wiewórcza Poczta, Poczta przez WWW
Summary(pt_BR):	O SquirrelMail é um webmail
Name:		squirrelmail
Version:	1.2.8
Release:	6
License:	GPL
Group:		Applications/Mail
Source0:	http://prdownloads.sf.net/squirrelmail/%{name}-%{version}.tar.bz2
Source1:	http://www.squirrelmail.org/plugins/%{name}_plugins-20010604.tar
Patch0:		%{name}-fortune.patch
Patch1:		%{name}-ri_once.patch
URL:		http://www.squirrelmail.org/
Requires:	webserver
Requires:	php
Requires:	php-gettext
Requires:	php-pcre
Provides:	webmail
Buildarch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_squirreldir	/home/httpd/html/squirrel

%description
This package contains the Squirrelmail, a webmail system which allows
you check mail by any cookie-aware WWW browser. It includes built-in
pure PHP support for the IMAP and SMTP protocols, and all pages render
in pure HTML 4.0 (with no Javascript) for maximum compatibility across
browsers. It has very few requirements and is very easy to configure
and install. SquirrelMail has a all the functionality you would want
from an email client, including strong MIME support, address books,
and folder manipulation.

%description -l pl
Pakiet zawiera Wiewiórcz±Pocztê, system pozwalaj±cy sprawdzaæ pocztê
przez dowoln±, obs³uguj±c± ciasteczka przegl±darkê WWW. Pakiet u¿ywa
wbudoewanego w PHP wsparcia do protoko³w IMAP i SMTP, a serwowane
strony u¿ywaj± tylko HTML 4.0 (bez Javascript) po to ¿eby udostêpniaæ
zasoby na mo¿liwie du¿± ilo¶æ typó³ pzregl±darek http. Pakiet jest
³atwy w instalacji i konfigurowaniu, a tak¿e ma wszystkie obecnie
wymagane cechy dobrego klienta pocztowego jak wsparcie do MIME,
ksia¿ka adresowa i wsparcie do pzrechowywaniu listów w folderach.

%description -l pt_BR
O SquirrelMail é um webmail baseado. Ele inclui suporte em PHP puro
para os protocolos IMAP e SMTP e todas as páginas são montadas em puro
HTML 4.0 (sem nenhum Javascript) para máxima compatibilidade entre
navegadores. Ele possui poucas exigências e é muito fácil de se
configurar e instalar. O SquirrelMail possui todas as funcionalidades
que você poderia desejar em um cliente de e-mail, incluindo um forte
suporte a MIME, livros de endereços e manipulação de pastas.

%package ispell
Summary:	A squirreel interface to ispel
Summary(pl):	Wiewórczy inerfejs do ispela
Group:		Applications/Mail
Requires:	ispell
Requires:	%{name} = %{version}
Provides:	webmail-spellcheck

%description ispell
This package contains a interface to ispell and it allows you to check
mail against typos and common mistakes

%description ispell -l pl
Pakiet zawiera interfejs do ispela pozwalaj±cy sprawdziæ pocztê pod
k±tem ¼le wpisanych s³ów i ortografi.

%package mailfetch
Summary:	A squirrel pop3 plug-in
Summary(pl):	Wiewiórczy plug-in pop3
Group:		Applications/Mail
Requires:	%{name} = %{version}

%description mailfetch
This package contains a interface to pop3 serwers, it allows you to
fetch mail from this kind of serwers.

%description mailfetch -l pl
Pakiet zawiera interfejs do serwerów pop3, pozwala ¶ci±gn±c z nich
pocztê za pomoc± us³ugi pop3.

%prep
%setup -q -a1

# List of usefull plugins (ONLY usefull one should be here)
for i in abook_take*tar.gz addgraphics*tar.gz attachment_common*tar.gz \
	auto_cc*tar.gz change_pass*tar.gz fortune*tar.gz gzip*tar.gz \
	mail_fwd*tar.gz motd*tar.gz password_forget*tar.gz username*tar.gz \
	printer_friendly*tar.gz quicksave*tar.gz retrieveuserdata*tar.gz \
	sqclock*tar.gz vacation*tar.gz; do
		tar xfvz $i -C plugins
done

%patch0 -p1
%patch1 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_squirreldir}/{config,data} \
	$RPM_BUILD_ROOT%{_datadir}/docs/squirrel/

cp -avR * $RPM_BUILD_ROOT%{_squirreldir}

cd $RPM_BUILD_ROOT
rm -rf `find . -name *.po`
cd -

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog INSTALL README ReleaseNotes UPGRADE doc/*.txt doc/*.html
%doc doc/README* doc/ReleaseNotes/1.2/*
%dir %{_squirreldir}
%attr(730,root,http) %dir %{_squirreldir}/data
%attr(640,root,http) %{_squirreldir}/data/.htaccess
%attr(640,root,http) %{_squirreldir}/data/*
%{_squirreldir}/index.php
%attr(744,root,root) %{_squirreldir}/configure
%attr(744,root,root) %{_squirreldir}/config/*.pl
%attr(640,root,http) %config(noreplace) %{_squirreldir}/config/*.php
%{_squirreldir}/functions
%dir %{_squirreldir}/help
%{_squirreldir}/help/index.php
%{_squirreldir}/help/en_US
%lang(ca) %{_squirreldir}/help/ca_ES
%lang(cs) %{_squirreldir}/help/cs_CZ
%lang(da) %{_squirreldir}/help/da_DK
%lang(es) %{_squirreldir}/help/es_ES
%lang(fi) %{_squirreldir}/help/fi_FI
%lang(fr) %{_squirreldir}/help/fr_FR
%lang(id) %{_squirreldir}/help/id_ID
%lang(it) %{_squirreldir}/help/it_IT
%lang(ko) %{_squirreldir}/help/ko_KR
%lang(lt) %{_squirreldir}/help/lt_LT
%lang(nl) %{_squirreldir}/help/nl_NL
%lang(pl) %{_squirreldir}/help/pl_PL
%lang(pt) %{_squirreldir}/help/pt_PT
%lang(pt_BR) %{_squirreldir}/help/pt_BR
%lang(ru) %{_squirreldir}/help/ru_RU
%lang(sl) %{_squirreldir}/help/sl_SI
%lang(sv) %{_squirreldir}/help/sv_SE
%lang(th) %{_squirreldir}/help/th_TH
%{_squirreldir}/images
%dir %{_squirreldir}/locale
%{_squirreldir}/locale/index.php
%{_squirreldir}/locale/timezones.cfg
%lang(bg) %{_squirreldir}/locale/bg_BG
%lang(ca) %{_squirreldir}/locale/ca_ES
%lang(da) %{_squirreldir}/locale/da_DK
%lang(de) %{_squirreldir}/locale/de_DE
%lang(cs) %{_squirreldir}/locale/cs_CZ
%lang(es) %{_squirreldir}/locale/es_ES
%lang(et) %{_squirreldir}/locale/et_EE
%lang(fi) %{_squirreldir}/locale/fi_FI
%lang(fr) %{_squirreldir}/locale/fr_FR
%lang(hr) %{_squirreldir}/locale/hr_HR
%lang(hu) %{_squirreldir}/locale/hu_HU
%lang(id) %{_squirreldir}/locale/id_ID
%lang(is) %{_squirreldir}/locale/is_IS
%lang(it) %{_squirreldir}/locale/it_IT
%lang(ko) %{_squirreldir}/locale/ko_KR
%lang(lt) %{_squirreldir}/locale/lt_LT
%lang(nl) %{_squirreldir}/locale/nl_NL
%lang(nn) %{_squirreldir}/locale/nn_NO
%lang(no) %{_squirreldir}/locale/no_NO
%lang(pl) %{_squirreldir}/locale/pl_PL
%lang(pt) %{_squirreldir}/locale/pt_PT
%lang(pt_BR) %{_squirreldir}/locale/pt_BR
%lang(ro) %{_squirreldir}/locale/ro_RO
%lang(ru) %{_squirreldir}/locale/ru_RU
%lang(sr) %{_squirreldir}/locale/sr_YU
%lang(sv) %{_squirreldir}/locale/sv_SE
%lang(sk) %{_squirreldir}/locale/sk_SK
%lang(sl) %{_squirreldir}/locale/sl_SI
%lang(th) %{_squirreldir}/locale/th_TH
%lang(tr) %{_squirreldir}/locale/tr_TR
%lang(zh_CN) %{_squirreldir}/locale/zh_CN
%lang(zh_TW) %{_squirreldir}/locale/zh_TW
%dir %{_squirreldir}/plugins
%{_squirreldir}/plugins/README.plugins
%{_squirreldir}/plugins/abook_take
%{_squirreldir}/plugins/addgraphics
%{_squirreldir}/plugins/administrator
%{_squirreldir}/plugins/attachment_common
%{_squirreldir}/plugins/auto_cc
%{_squirreldir}/plugins/bug_report
%{_squirreldir}/plugins/calendar
%{_squirreldir}/plugins/change_pass
%{_squirreldir}/plugins/delete_move_next
%{_squirreldir}/plugins/filters
%{_squirreldir}/plugins/fortune
%{_squirreldir}/plugins/gzip
%{_squirreldir}/plugins/index.php
%{_squirreldir}/plugins/info
%{_squirreldir}/plugins/listcommands
%{_squirreldir}/plugins/mail_fwd
%{_squirreldir}/plugins/make_archive.pl
%{_squirreldir}/plugins/motd
%{_squirreldir}/plugins/newmail
%{_squirreldir}/plugins/password_forget
%{_squirreldir}/plugins/printer_friendly
%{_squirreldir}/plugins/quicksave
%{_squirreldir}/plugins/retrieveuserdata
%{_squirreldir}/plugins/sent_subfolders
%{_squirreldir}/plugins/spamcop
%{_squirreldir}/plugins/sqclock
%{_squirreldir}/plugins/translate
%{_squirreldir}/plugins/username
%{_squirreldir}/plugins/vacation
%{_squirreldir}/src
%{_squirreldir}/themes

%files ispell
%defattr(644,root,root,755)
%{_squirreldir}/plugins/squirrelspell

%files mailfetch
%defattr(644,root,root,755)
%{_squirreldir}/plugins/mail_fetch
