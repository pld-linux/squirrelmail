# TODO:
# - make separate packages with plugins
# - move plugins into separate specs
#
Summary:	The SquirrelMail, a WebMail package
Summary(pl):	Wiewiórcza Poczta, Poczta przez WWW
Summary(pt_BR):	O SquirrelMail é um webmail
Name:		squirrelmail
Version:	1.4.6
%define		_rc	rc1
Release:	0.%{_rc}.2
License:	GPL
Group:		Applications/Mail
Source0:	http://dl.sourceforge.net/squirrelmail/%{name}-%{version}-%{_rc}.tar.bz2
# Source0-md5:	9e58e290f6a40df2798f9c21fe460223
%define		_all_locales_date	20051212
Source1:	http://dl.sourceforge.net/squirrelmail/all_locales-%{version}%{_rc}-%{_all_locales_date}.tar.bz2
# Source1-md5:	016f41abaee2c1a9d9f4b3c0bd8efbea
%define		_compatibility_version	2.0.4
Source2:	http://www.squirrelmail.org/plugins/compatibility-%{_compatibility_version}.tar.gz
# Source2-md5:	cfc3279a613b917fcba8200c596dadb0
Source3:	http://www.squirrelmail.org/plugins/addgraphics-2.3-1.0.3.tar.gz
# Source3-md5:	c9319e32149026372a0d515ddbc1d14b
Source4:	http://www.squirrelmail.org/plugins/auto_cc-2.0-1.2.tar.gz
# Source4-md5:	259a001d964c7257be11bbb2b764ba52
Source5:	http://www.squirrelmail.org/plugins/change_pass-2.7-1.4.x.tar.gz
# Source5-md5:	590e0b3e879bffdb4dea57d369618353
Source6:	http://www.squirrelmail.org/plugins/gzip-2.02-1.1.1.tar.gz
# Source6-md5:	2df7370e0dbdf3e48e888cef094ead8b
Source7:	http://www.squirrelmail.org/plugins/mail_fwd.0.4.1-1.4.0.tar.gz
# Source7-md5:	472bfb19e60d865b7aa363f3ea0293c2
Source8:	http://www.squirrelmail.org/plugins/motd.1.2-1.0.3.tar.gz
# Source8-md5:	d76f2f5282dfc4a4c90dc28326d92b4b
Source9:	http://www.squirrelmail.org/plugins/password_forget.2.1-1.0.1.tar.gz
# Source9-md5:	33ffd387d5190b690d53358cb3b4e691
Source10:	http://www.squirrelmail.org/plugins/quicksave-2.3-1.1.0.tar.gz
# Source10-md5:	c60c68aace4eb67ccba4282327b13fdc
Source11:	http://www.squirrelmail.org/plugins/retrieveuserdata.0.9-1.4.0.tar.gz
# Source11-md5:	dfe469f7ab473fd2292b30800e3141d5
Source12:	http://www.squirrelmail.org/plugins/username-2.3-1.0.0.tar.gz
# Source12-md5:	c81670f5607835dc1e226653cf5c53b1
Source13:	http://www.squirrelmail.org/plugins/vacation_1.41_1.4.tar.gz
# Source13-md5:	f1fbd5e3778bd8bcae41ca147fbc4333
Source14:	%{name}.conf
#%define		_change_passwd_version	4.0
#SourceX:	http://www.squirrelmail.org/plugins/change_passwd-%{_change_passwd_version}-1.2.8.tar.gz
## SourceX-md5:	22b5ee1698b2e59a88f2150a96ec17f3
Patch0:		%{name}-config.patch
Patch1:		%{name}-ri_once.patch
Patch2:		%{name}-fortune.patch
Patch3:		%{name}-mail_fwd-Makefile.patch
Patch4:		%{name}-squirrelspell.patch
Patch5:		%{name}-retrieveuserdata-passwd.patch
URL:		http://www.squirrelmail.org/
BuildRequires:	bind-devel
BuildRequires:	gettext-devel
BuildRequires:	rpmbuild(macros) >= 1.264
Requires:	php
Requires:	php-gettext
Requires:	php-pcre
Requires:	php-posix
Requires:	php-zlib
Requires:	webapps
Requires:	webserver
Provides:	squirrelmail-compatibility-%{_compatibility_version}
Provides:	webmail
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_squirreldir	%{_datadir}/%{name}
%define		_squirreldata	/var/lib/%{name}
%define		_webapps		/etc/webapps
%define		_webapp			%{name}
%define		_sysconfdir		%{_webapps}/%{_webapp}

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
Pakiet zawiera Wiewiórcz± Pocztê, system pozwalaj±cy sprawdzaæ pocztê
przez dowoln±, obs³uguj±c± ciasteczka przegl±darkê WWW. Pakiet u¿ywa
wbudowanej w PHP obs³ugi protoko³ów IMAP i SMTP, a serwowane strony
u¿ywaj± tylko HTML 4.0 (bez Javascriptu) po to, ¿eby udostêpniaæ
zasoby na mo¿liwie du¿± ilo¶æ typów przegl±darek http. Pakiet jest
³atwy w instalacji i konfigurowaniu, a tak¿e ma wszystkie obecnie
wymagane cechy dobrego klienta pocztowego jak obs³uga MIME, ksi±¿ka
adresowa i wsparcie dla przechowywania listów w folderach.

%description -l pt_BR
O SquirrelMail é um webmail baseado. Ele inclui suporte em PHP puro
para os protocolos IMAP e SMTP e todas as páginas são montadas em puro
HTML 4.0 (sem nenhum Javascript) para máxima compatibilidade entre
navegadores. Ele possui poucas exigências e é muito fácil de se
configurar e instalar. O SquirrelMail possui todas as funcionalidades
que você poderia desejar em um cliente de e-mail, incluindo um forte
suporte a MIME, livros de endereços e manipulação de pastas.

%package change_pass
Summary:	A squirrel interface to change passwords
Summary(pl):	Wiewiórczy interfejs do zmiany hase³
Group:		Applications/Mail
Requires:	%{name} = %{version}-%{release}
Requires:	poppassd
Requires:	squirrelmail-compatibility-%{_compatibility_version}

%description change_pass
This package contains an interface to change passwords.

%description change_pass -l pl
Ten pakiet zawiera interfejs do zmiany hase³.

%package filters
Summary:	A squirrel interface for various filters
Summary(pl):	Wiewiórczy interfejs do ró¿nych filterów
Group:		Applications/Mail
Requires:	%{name} = %{version}-%{release}
Provides:	webmail-filters

%description filters
This package contains an interface for various filters.

%description filters -l pl
Ten pakiet zawiera interfejs do ró¿nych filtrów.

%package ispell
Summary:	A squirrel interface to ispell
Summary(pl):	Wiewiórczy interfejs do ispella
Group:		Applications/Mail
Requires:	%{name} = %{version}-%{release}
Requires:	ispell
Provides:	webmail-spellcheck

%description ispell
This package contains an interface to ispell and it allows you to
check mail against typos and common mistakes.

%description ispell -l pl
Pakiet zawiera interfejs do ispella pozwalaj±cy sprawdziæ pocztê pod
k±tem ¼le wpisanych s³ów i ortografii.

%package mail_fwd
Summary:	A squirrel email forwarding plug-in
Summary(pl):	Wtyczka umo¿liwiaj±ca przekierowanie poczty
Group:		Applications/Mail
Requires:	%{name} = %{version}-%{release}

%description mail_fwd
This plug-in allows to set email forwarding.
Note: binary file included in this package must be suid.

%description mail_fwd -l pl
Ta wtyczka pozwala na ustawienie przekierowania poczty.
Uwaga: plik binarny zawarty w tym pakiecie musi mieæ ustawiony bit
suid.

%package mailfetch
Summary:	A squirrel pop3 plug-in
Summary(pl):	Wiewiórcza wtyczka pop3
Group:		Applications/Mail
Requires:	%{name} = %{version}-%{release}

%description mailfetch
This package contains a interface to pop3 serwers, it allows you to
fetch mail from this kind of serwers.

%description mailfetch -l pl
Pakiet zawiera interfejs do serwerów pop3, pozwala ¶ci±gaæ z nich
pocztê za pomoc± us³ugi pop3.

%package newmail
Summary:	A new mail notify plug-in
Summary(pl):	Wtyczka informuj±ca o nowej poczcie
Group:		Applications/Mail
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-ispell = %{version}-%{release}

%description newmail
A Squirrel new mail notify plug-in.

%description newmail -l pl
Wiewiórcza wtyczka informuj±ca o nowej poczcie.

%package vacation
Summary:	A vacation plugin
Summary(pl):	Wtyczka vacation
Group:		Applications/Mail
Requires:	%{name} = %{version}-%{release}
Requires:	php-ftp

%description vacation
A Squirrel vacation plug-in.

%description vacation -l pl
Wtyczka vacation dla Squirrelmaila.

%prep
%setup -q -a1 -n %{name}-%{version}-%{_rc}

for f in %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7} \
	%{SOURCE8} %{SOURCE9} %{SOURCE10} %{SOURCE11} %{SOURCE12} %{SOURCE13}; do
	tar -xzf $f -C plugins
done

# locales for not present plugins
rm -f locale/*/LC_MESSAGES/{abook_group,address_add,admin_add,amavisnewsql,archive_mail,askuserinfo,attachment_doc,autocomplete,avelsieve,block_attach,block_sender,bounce,change_ldappass,change_merakpass,change_mysqlpass,change_passwd,check_quota,chg_sasl_passwd,contactclean,cookie_warning,courier_vacation,custom_from,disk_quota,empty_folders,enews,extract,file_manager,folder_sizes,gpg,got_hotmail,image_buttons,japanese_input,junkfolder,ldap_abook,ldapquery,left_css,login_alias,mark_read,naguser,notes,online_users,preview_pane,qmailadmin_login,quota_usage,restrict_senders,rewrap,sasql,select_range,sent_confirmation,serversidefilter,show_headers,show_user_and_ip,smallcal,smime,startup_folder,tmda,tmdatools,taglines,templates,timeout_user,twc_weather,unsafe_image_rules,useracl,user_special_mailboxes,vadmin,view_as_html,virus_scan,vkeyboard,vpopmail,windows,yelp}.mo

# move to proper place (set by bindtextdomain in plugin)
for f in `find locale -name change_pass.mo`; do
	if [ ! -f plugins/change_pass/$f ]; then
		install -D $f plugins/change_pass/$f
	fi
	rm -f $f
done
for f in `find locale -name gzip.mo`; do
	if [ ! -f plugins/gzip/$f ]; then
		install -D $f plugins/gzip/$f
	fi
	rm -f $f
done

# missing (bind)textdomain calls?
# auto_cc, compatibility, quicksave, username, vacation

#rm -f plugins/change_passwd/chpasswd
rm -f plugins/mail_fwd/fwdfile/wfwd.o

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

find locale -name '*.po' | xargs rm -f

%build
%{__make} -C plugins/mail_fwd/fwdfile \
	CFLAGS="%{rpmcflags}" \
	LFLAGS="%{rpmldflags}"

%{__make} -C plugins/filters/bulkquery \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} " \
	LDFLAGS="%{rpmldflags} -lpthread -llwres" \

#%{__cc} %{rpmldflags} %{rpmcflags} -Wall -o plugins/change_passwd/chpasswd \
#	plugins/change_passwd/chpasswd.c -lcrypt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_squirreldir}/{config,data},%{_sbindir}} \
	$RPM_BUILD_ROOT{%{_datadir}/docs/squirrel,%{_squirreldata}/{prefs,data}} \
	$RPM_BUILD_ROOT%{_sysconfdir}

install plugins/mail_fwd/fwdfile/wfwd $RPM_BUILD_ROOT%{_sbindir}
install plugins/filters/bulkquery/bulkquery $RPM_BUILD_ROOT%{_sbindir}
rm -f plugins/filters/bulkquery/*.{in,out,c} plugins/filters/bulkquery/bulkquery

install %{SOURCE14} $RPM_BUILD_ROOT%{_sysconfdir}/httpd.conf
install %{SOURCE14} $RPM_BUILD_ROOT%{_sysconfdir}/apache.conf

cp -aR * $RPM_BUILD_ROOT%{_squirreldir}

find $RPM_BUILD_ROOT%{_squirreldir} -name '*.po' -o -name '*.pot' | xargs rm -f

# junk:
rm -f $RPM_BUILD_ROOT%{_squirreldir}/plugins/{username/options.php,gzip/setup.php~,make_archive.pl,README.plugins}

ln -s %{_sbindir}/bulkquery $RPM_BUILD_ROOT%{_squirreldir}/plugins/filters/bulkquery/bulkquery

##---{ move configuration to etc: }---##
cp $RPM_BUILD_ROOT{%{_squirreldir}/config/config_default.php,%{_sysconfdir}/config.php}
ln -sf %{_sysconfdir}/config.php $RPM_BUILD_ROOT%{_squirreldir}/config/config.php

##---{ move plugins configuration to etc: }---##
# vacation:
mv $RPM_BUILD_ROOT%{_squirreldir}/plugins/vacation/config.php $RPM_BUILD_ROOT%{_sysconfdir}/vacation_config.php
ln -s %{_sysconfdir}/vacation_config.php $RPM_BUILD_ROOT%{_squirreldir}/plugins/vacation/config.php
# filters:
mv $RPM_BUILD_ROOT%{_squirreldir}/plugins/filters/setup.php $RPM_BUILD_ROOT%{_sysconfdir}/filters_setup.php
ln -s %{_sysconfdir}/filters_setup.php $RPM_BUILD_ROOT%{_squirreldir}/plugins/filters/setup.php

##---{ Other manipulations: }---##
mv $RPM_BUILD_ROOT%{_squirreldir}/plugins/filters/bulkquery/README $RPM_BUILD_ROOT%{_squirreldir}/plugins/filters/README.bulkquery
mv $RPM_BUILD_ROOT%{_squirreldir}/plugins/filters/bulkquery/INSTALL $RPM_BUILD_ROOT%{_squirreldir}/plugins/filters/INSTALL.bulkquery

%clean
rm -rf $RPM_BUILD_ROOT

%triggerin -- apache1
%webapp_register apache %{_webapp}

%triggerun -- apache1
%webapp_unregister apache %{_webapp}

%triggerin -- apache >= 2.0.0
%webapp_register httpd %{_webapp}

%triggerun -- apache >= 2.0.0
%webapp_unregister httpd %{_webapp}

%triggerpostun -- squirrelmail < 1.4.5-4.1
if [ -f /home/services/httpd/html/squirrel/config/config.php.rpmsave ]; then
	echo "Moving old config file to %{_sysconfdir}/config.php"
	mv -f %{_sysconfdir}/config.php{,.rpmnew}
	mv -f /home/services/httpd/html/squirrel/config/config.php.rpmsave %{_sysconfdir}/config.php
fi

if [ -f /etc/squirrelmail/config.php.rpmsave ]; then
	echo "Moving old config file to %{_sysconfdir}/config.php"
	mv -f %{_sysconfdir}/config.php{,.rpmnew}
	mv -f /etc/squirrelmail/config.php.rpmsave %{_sysconfdir}/config.php
fi

# nuke very-old config location (this mostly for Ra)
if [ -f /etc/httpd/httpd.conf ]; then
	sed -i -e "/^Include.*squirrelmail.conf/d" /etc/httpd/httpd.conf
	httpd_reload=1
fi

# migrate from httpd (apache2) config dir
if [ -f /etc/httpd/squirrelmail.conf.rpmsave ]; then
	cp -f %{_sysconfdir}/httpd.conf{,.rpmnew}
	mv -f /etc/httpd/squirrelmail.conf.rpmsave %{_sysconfdir}/httpd.conf
	httpd_reload=1
fi

if [ -d /etc/httpd/webapps.d ]; then
	/usr/sbin/webapp register httpd %{_webapp}
	httpd_reload=1
fi

# place new config location, as trigger puts config only on first install, do it here.
if [ -L /etc/httpd/httpd.conf/99_squirrelmail.conf ]; then
	rm -f /etc/httpd/httpd.conf/99_squirrelmail.conf
	/usr/sbin/webapp register httpd %{_webapp}
	httpd_reload=1
fi

if [ "$httpd_reload" ]; then
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd reload 1>&2
	fi
fi

%triggerpostun vacation -- squirrelmail-vacation < 1.4.5-4.1
if [ -f /etc/squirrelmail/vacation_config.php.rpmsave ]; then
	echo "Moving old config file to %{_sysconfdir}/vacation_config.php"
	mv -f %{_sysconfdir}/vacation_config.php{,.rpmnew}
	mv -f /etc/squirrelmail/vacation_config.php.rpmsave %{_sysconfdir}/vacation_config.php
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog ChangeLog.locales README ReleaseNotes ReleaseNotes.locales UPGRADE doc/*.txt doc/*.html
%doc doc/ReleaseNotes/*/*

%dir %attr(750,root,http) %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/apache.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/config.php

%dir %{_squirreldir}
%{_squirreldir}/class
%attr(640,root,http) %{_squirreldir}/data/.htaccess
%attr(640,root,http) %{_squirreldir}/data/*
%{_squirreldir}/index.php
%attr(744,root,root) %{_squirreldir}/configure
%attr(750,root,http) %dir %{_squirreldir}/config
%attr(744,root,root) %{_squirreldir}/config/*.pl
%attr(640,root,http) %config(noreplace) %{_squirreldir}/config/*.php
%{_squirreldir}/functions
%dir %{_squirreldir}/help
%{_squirreldir}/help/index.php
%{_squirreldir}/help/en_US
%lang(bg) %{_squirreldir}/help/bg_BG
%lang(ca) %{_squirreldir}/help/ca_ES
%lang(cs) %{_squirreldir}/help/cs_CZ
%lang(cy) %{_squirreldir}/help/cy_GB
%lang(da) %{_squirreldir}/help/da_DK
%lang(de) %{_squirreldir}/help/de_DE
%lang(en) %{_squirreldir}/help/en_GB
%lang(es) %{_squirreldir}/help/es_ES
%lang(fi) %{_squirreldir}/help/fi_FI
%lang(fr) %{_squirreldir}/help/fr_FR
%lang(id) %{_squirreldir}/help/id_ID
%lang(it) %{_squirreldir}/help/it_IT
%lang(ja) %{_squirreldir}/help/ja_JP
%lang(ko) %{_squirreldir}/help/ko_KR
%lang(lt) %{_squirreldir}/help/lt_LT
%lang(nl) %{_squirreldir}/help/nl_NL
%lang(pl) %{_squirreldir}/help/pl_PL
%lang(pt) %{_squirreldir}/help/pt_PT
%lang(pt_BR) %{_squirreldir}/help/pt_BR
%lang(ru) %{_squirreldir}/help/ru_RU
%lang(sk) %{_squirreldir}/help/sk_SK
%lang(sl) %{_squirreldir}/help/sl_SI
%lang(sr) %{_squirreldir}/help/sr_YU
%lang(sv) %{_squirreldir}/help/sv_SE
%lang(th) %{_squirreldir}/help/th_TH
%lang(zh_CN) %{_squirreldir}/help/zh_CN
%{_squirreldir}/images
%{_squirreldir}/include
%dir %{_squirreldir}/locale
%{_squirreldir}/locale/index.php
%{_squirreldir}/locale/timezones.cfg
%lang(ar) %{_squirreldir}/locale/ar
%lang(bg) %{_squirreldir}/locale/bg_BG
%lang(bn) %{_squirreldir}/locale/bn_IN
%lang(ca) %{_squirreldir}/locale/ca_ES
%lang(da) %{_squirreldir}/locale/da_DK
%lang(de) %{_squirreldir}/locale/de_DE
%lang(cs) %{_squirreldir}/locale/cs_CZ
%lang(cy) %{_squirreldir}/locale/cy_GB
%lang(el) %{_squirreldir}/locale/el_GR
%lang(en) %{_squirreldir}/locale/en_GB
%lang(es) %{_squirreldir}/locale/es_ES
%lang(eu) %{_squirreldir}/locale/eu_ES
%lang(fa) %{_squirreldir}/locale/fa_IR
%lang(fi) %{_squirreldir}/locale/fi_FI
%lang(fo) %{_squirreldir}/locale/fo_FO
%lang(fr) %{_squirreldir}/locale/fr_FR
%lang(he) %{_squirreldir}/locale/he_IL
%lang(hr) %{_squirreldir}/locale/hr_HR
%lang(hu) %{_squirreldir}/locale/hu_HU
%lang(id) %{_squirreldir}/locale/id_ID
%lang(is) %{_squirreldir}/locale/is_IS
%lang(it) %{_squirreldir}/locale/it_IT
%lang(ja) %{_squirreldir}/locale/ja_JP
%lang(ko) %{_squirreldir}/locale/ko_KR
%lang(lt) %{_squirreldir}/locale/lt_LT
%lang(ms) %{_squirreldir}/locale/ms_MY
%lang(nb) %{_squirreldir}/locale/nb_NO
%lang(nl) %{_squirreldir}/locale/nl_NL
%lang(nn) %{_squirreldir}/locale/nn_NO
%lang(pl) %{_squirreldir}/locale/pl_PL
%lang(pt) %{_squirreldir}/locale/pt_PT
%lang(pt_BR) %{_squirreldir}/locale/pt_BR
%lang(ro) %{_squirreldir}/locale/ro_RO
%lang(ru) %{_squirreldir}/locale/ru_RU
%lang(sr) %{_squirreldir}/locale/sr_YU
%lang(sv) %{_squirreldir}/locale/sv_SE
%lang(sk) %{_squirreldir}/locale/sk_SK
%lang(sl) %{_squirreldir}/locale/sl_SI
#%lang(th) %{_squirreldir}/locale/th_TH
%lang(tr) %{_squirreldir}/locale/tr_TR
%lang(ug) %{_squirreldir}/locale/ug
#%lang(uk) %{_squirreldir}/locale/uk_UA
#%lang(vi) %{_squirreldir}/locale/vi_VN
%lang(zh_CN) %{_squirreldir}/locale/zh_CN
%lang(zh_TW) %{_squirreldir}/locale/zh_TW
%dir %{_squirreldir}/plugins
%{_squirreldir}/plugins/abook_take
%{_squirreldir}/plugins/addgraphics
%{_squirreldir}/plugins/administrator
%{_squirreldir}/plugins/auto_cc
%{_squirreldir}/plugins/bug_report
%{_squirreldir}/plugins/calendar
%{_squirreldir}/plugins/compatibility
%{_squirreldir}/plugins/delete_move_next
%{_squirreldir}/plugins/fortune
%dir %{_squirreldir}/plugins/gzip
%{_squirreldir}/plugins/gzip/*.php
%dir %{_squirreldir}/plugins/gzip/locale
%lang(el) %{_squirreldir}/plugins/gzip/locale/el_GR
%{_squirreldir}/plugins/index.php
%{_squirreldir}/plugins/info
%{_squirreldir}/plugins/listcommands
%{_squirreldir}/plugins/message_details
%{_squirreldir}/plugins/motd
%{_squirreldir}/plugins/password_forget
%{_squirreldir}/plugins/quicksave
%{_squirreldir}/plugins/retrieveuserdata
%{_squirreldir}/plugins/sent_subfolders
%{_squirreldir}/plugins/spamcop
%{_squirreldir}/plugins/translate
%{_squirreldir}/plugins/username
%{_squirreldir}/src
%{_squirreldir}/themes
%attr(710,root,http) %dir %{_squirreldata}
%attr(730,root,http) %dir %{_squirreldata}/prefs
%attr(730,root,http) %dir %{_squirreldata}/data
# To be removed. Just for compatibility with existing configurations:
%attr(730,root,http) %dir %{_squirreldir}/data

%files change_pass
%defattr(644,root,root,755)
%doc plugins/change_pass/README
%dir %{_squirreldir}/plugins/change_pass
%dir %{_squirreldir}/plugins/change_pass/locale
%{_squirreldir}/plugins/change_pass/*.php
%lang(bg) %{_squirreldir}/plugins/change_pass/locale/bg_BG
%lang(de) %{_squirreldir}/plugins/change_pass/locale/de_DE
%lang(es) %{_squirreldir}/plugins/change_pass/locale/es_ES
%lang(fr) %{_squirreldir}/plugins/change_pass/locale/fr_FR
%lang(ja) %{_squirreldir}/plugins/change_pass/locale/ja_JP
%lang(lt) %{_squirreldir}/plugins/change_pass/locale/lt_LT
%lang(pl) %{_squirreldir}/plugins/change_pass/locale/pl_PL
%lang(pt_BR) %{_squirreldir}/plugins/change_pass/locale/pt_BR
%lang(pt) %{_squirreldir}/plugins/change_pass/locale/pt_PT

%files filters
%defattr(644,root,root,755)
%doc plugins/filters/{README*,CHANGES}
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/filters_setup.php
%attr(755,root,root) %{_sbindir}/bulkquery
%dir %{_squirreldir}/plugins/filters
%dir %{_squirreldir}/plugins/filters/bulkquery
%{_squirreldir}/plugins/filters/*.php

%files ispell
%defattr(644,root,root,755)
%{_squirreldir}/plugins/squirrelspell

%files mail_fwd
%defattr(644,root,root,755)
%doc plugins/mail_fwd/README
%attr(755,root,root) %{_sbindir}/wfwd
%dir %{_squirreldir}/plugins/mail_fwd
%{_squirreldir}/plugins/mail_fwd/[!f]*.php

%files mailfetch
%defattr(644,root,root,755)
%doc plugins/mail_fetch/README
%dir %{_squirreldir}/plugins/mail_fetch
%{_squirreldir}/plugins/mail_fetch/*.php

%files newmail
%defattr(644,root,root,755)
%doc plugins/newmail/{HISTORY,README}
%dir %{_squirreldir}/plugins/newmail
%{_squirreldir}/plugins/newmail/*.php
%{_squirreldir}/plugins/newmail/sounds

%files vacation
%defattr(644,root,root,755)
%doc plugins/vacation/README
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/vacation_config.php
%dir %{_squirreldir}/plugins/vacation
%{_squirreldir}/plugins/vacation/*.php
