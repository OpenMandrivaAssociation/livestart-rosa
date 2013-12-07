Summary:	Livestart rosa script
Name:		livestart-rosa
Version:	1.0.0
Release:	11
BuildArch:	noarch
License:	GPL
Group:		System/Configuration/Other
Source10:	checkflashboot
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Small script checking if system was started from a
flash drive and creating a config for draklive-install.

%post
%_post_service checkflashboot

%preun
%_preun_service checkflashboot

%files
%defattr(-,root,root)
%attr(755,root,root) %_sysconfdir/init.d/checkflashboot

#--------------------------------------------------------------------

%install
rm -rf %buildroot 

mkdir -p %buildroot%_sysconfdir/init.d/
cp %SOURCE10 %buildroot%_sysconfdir/init.d/



%changelog
* Wed May 04 2011 Eugeni Dodonov <eugeni@mandriva.com> 1.0.0-3
+ Revision: 666397
- Properly install and uninstall service.

* Wed Apr 06 2011 Alex Burmashev <burmashev@mandriva.org> 1.0.0-2
+ Revision: 650866
- Small edit to prevent overwriting existing config
- Small edit to prevent overwriting existing config

* Tue Apr 05 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.0.0-1
+ Revision: 650682
- Several cosmetics

  + Alex Burmashev <burmashev@mandriva.org>
    - import livestart-rosa

