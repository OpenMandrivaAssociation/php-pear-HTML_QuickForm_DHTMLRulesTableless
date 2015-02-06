%define		_class		HTML
%define		_subclass	QuickForm
%define		upstream_name	%{_class}_%{_subclass}_DHTMLRulesTableless

Name:		php-pear-%{upstream_name}
Version:	0.3.3
Release:	2
Summary:	DHTML replacement for the standard JavaScript alert window 
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/HTML_QuickForm_DHTMLRulesTableless
Source0:	http://download.pear.php.net/package/HTML_QuickForm_DHTMLRulesTableless-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
DHTML replacement for the standard JavaScript alert window for client-side
validation using the tableless renderer

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/examples
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3.2-8mdv2012.0
+ Revision: 741997
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3.2-7
+ Revision: 679348
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.2-6mdv2011.0
+ Revision: 613674
- the mass rebuild of 2010.1 packages

* Sat Dec 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.2-5mdv2010.1
+ Revision: 477874
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.3.2-4mdv2010.0
+ Revision: 441121
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.3.2-3mdv2009.1
+ Revision: 322116
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3.2-2mdv2009.0
+ Revision: 236875
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 0.3.2-1mdv2008.1
+ Revision: 136407
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Aug 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.3.2-1mdv2008.0
+ Revision: 68587
- Import php-pear-HTML_QuickForm_DHTMLRulesTableless



* Tue Aug 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.3.2-1mdv2008.0
- initial Mandriva package

