Summary:	Livestart rosa script
Name:		livestart-rosa
Version:	1.0.0
Release:	%mkrel 2
BuildArch:	noarch
License:	GPL
Group:		System/Configuration/Other
Source10:	checkflashboot
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot


%description
Small script checking if system was started from a 
flash drive and creating a config for draklive-install.

%install
rm -rf $RPM_BUILD_ROOT 

mkdir -p $RPM_BUILD_ROOT/etc/init.d/
cp %SOURCE10 $RPM_BUILD_ROOT/etc/init.d/

%post
/sbin/chkconfig --add checkflashboot
/sbin/chkconfig --level 2345 checkflashboot

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(755,root,root) /etc/init.d/checkflashboot

