Name:		envycontrol
Version:	3.5.2
Release:	2
URL:		https://github.com/bayasdev/envycontrol
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Summary:	Easy GPU switching for Nvidia Optimus laptops
License:	MIT
Group:		Terminal/Utilities
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
%summary

%files
%{_bindir}/%{name}
%{py_sitedir}/envycontrol.py
%{py_sitedir}/envycontrol-*.*-info
