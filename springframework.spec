Name:                springframework
Version:             3.2.18
Release:             8
Summary:             The Spring Java Application Framework
License:             ASL 2.0
URL:                 http://projects.spring.io/spring-framework/
Source0:             https://github.com/spring-projects/spring-framework/archive/v3.2.18.RELEASE/springframework-3.2.18.RELEASE.tar.gz
Source101:           springframework-3.2.18.RELEASE.pom
Source102:           https://repo1.maven.org/maven2/org/springframework/spring-core/3.2.18.RELEASE/spring-core-3.2.18.RELEASE.pom
Source103:           https://repo1.maven.org/maven2/org/springframework/spring-expression/3.2.18.RELEASE/spring-expression-3.2.18.RELEASE.pom
Source104:           https://repo1.maven.org/maven2/org/springframework/spring-context/3.2.18.RELEASE/spring-context-3.2.18.RELEASE.pom
Source105:           https://repo1.maven.org/maven2/org/springframework/spring-aop/3.2.18.RELEASE/spring-aop-3.2.18.RELEASE.pom
Source106:           https://repo1.maven.org/maven2/org/springframework/spring-instrument/3.2.18.RELEASE/spring-instrument-3.2.18.RELEASE.pom
Source107:           https://repo1.maven.org/maven2/org/springframework/spring-beans/3.2.18.RELEASE/spring-beans-3.2.18.RELEASE.pom
Source108:           https://repo1.maven.org/maven2/org/springframework/spring-orm/3.2.18.RELEASE/spring-orm-3.2.18.RELEASE.pom
Source109:           https://repo1.maven.org/maven2/org/springframework/spring-test/3.2.18.RELEASE/spring-test-3.2.18.RELEASE.pom
Source111:           https://repo1.maven.org/maven2/org/springframework/spring-instrument-tomcat/3.2.18.RELEASE/spring-instrument-tomcat-3.2.18.RELEASE.pom
Source112:           https://repo1.maven.org/maven2/org/springframework/spring-jdbi/3.2.18.RELEASE/spring-jdbc-3.2.18.RELEASE.pom
Source113:           https://repo1.maven.org/maven2/org/springframework/spring-jms/3.2.18.RELEASE/spring-jms-3.2.18.RELEASE.pom
Source114:           https://repo1.maven.org/maven2/org/springframework/spring-tx/3.2.18.RELEASE/spring-tx-3.2.18.RELEASE.pom
Source115:           https://repo1.maven.org/maven2/org/springframework/spring-web/3.2.18.RELEASE/spring-web-3.2.18.RELEASE.pom
Source116:           https://repo1.maven.org/maven2/org/springframework/spring-oxm/3.2.18.RELEASE/spring-oxm-3.2.18.RELEASE.pom
Source120:           spring-test-mvc-3.2.18.RELEASE.pom
Source121:           spring-orm-hibernate4-template.pom
Patch0:              springframework-3.2.6-java.io.IOException-is-never-thrown.patch
Patch1:              springframework-3.2.6-port-spring-jms-to-javax.resources-1.7.patch
Patch2:              springframework-3.2.6-port-spring-orm-to-javax.persistence-2.0.patch
Patch3:              springframework-3.2.6-port-spring-test-to-servlet-3.1.patch
Patch4:              springframework-3.2.6-port-spring-tx-to-javax.resources-1.7.patch
Patch5:              springframework-3.2.6-port-to-hibernate-validator-5.patch
Patch6:              springframework-3.2.13-derby.patch
Patch7:              springframework-3.2.14-jopt-simple.patch
Patch8:              springframework-3.2.14-build-with-tomcat8.patch
Patch9:              springframework-3.2.18-hibernate4.3.patch
Patch10:             CVE-2020-5421.patch
patch11:	     CVE-2016-5007.patch
BuildRequires:       maven-local mvn(aopalliance:aopalliance) mvn(c3p0:c3p0) mvn(com.caucho:hessian)
BuildRequires:       mvn(com.fasterxml.jackson.core:jackson-databind) mvn(com.h2database:h2)
BuildRequires:       mvn(com.jamonapi:jamon) mvn(com.rometools:rome)
BuildRequires:       mvn(commons-beanutils:commons-beanutils)
BuildRequires:       mvn(commons-fileupload:commons-fileupload)
BuildRequires:       mvn(commons-httpclient:commons-httpclient) mvn(commons-io:commons-io)
BuildRequires:       mvn(commons-logging:commons-logging) mvn(commons-pool:commons-pool)
BuildRequires:       mvn(com.thoughtworks.xstream:xstream) mvn(hsqldb:hsqldb:1)
BuildRequires:       mvn(javax.ejb:ejb-api)
BuildRequires:       mvn(javax.faces:jsf-api) mvn(javax.inject:javax.inject) mvn(javax.jdo:jdo-api)
BuildRequires:       mvn(javax.mail:mail) mvn(javax.portlet:portlet-api)
BuildRequires:       mvn(javax.servlet:javax.servlet-api) mvn(javax.servlet.jsp:jsp-api)
BuildRequires:       mvn(javax.servlet:jstl) mvn(javax.servlet:servlet-api)
BuildRequires:       mvn(javax.xml:jaxrpc-api) mvn(javax.xml.soap:saaj-api) mvn(joda-time:joda-time)
BuildRequires:       mvn(junit:junit) mvn(log4j:log4j) mvn(net.sf.cglib:cglib)
BuildRequires:       mvn(net.sf.ehcache:ehcache-core) mvn(net.sourceforge.jexcelapi:jxl)
BuildRequires:       mvn(org.apache.derby:derby) mvn(org.apache.derby:derbyclient)
BuildRequires:       mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:       mvn(org.apache.geronimo.specs:geronimo-interceptor_3.0_spec)
BuildRequires:       mvn(org.apache.geronimo.specs:geronimo-jms_1.1_spec)
BuildRequires:       mvn(org.apache.geronimo.specs:geronimo-jta_1.1_spec)
BuildRequires:       mvn(org.apache.geronimo.specs:geronimo-validation_1.0_spec)
BuildRequires:       mvn(org.apache.httpcomponents:httpclient) mvn(org.apache.openjpa:openjpa-lib)
BuildRequires:       mvn(org.apache.openjpa:openjpa-persistence) mvn(org.apache.poi:poi)
BuildRequires:       mvn(org.apache.tiles:tiles-api)
BuildRequires:       mvn(org.apache.tiles:tiles-core) mvn(org.apache.tiles:tiles-el)
BuildRequires:       mvn(org.apache.tiles:tiles-jsp) mvn(org.apache.tiles:tiles-servlet)
BuildRequires:       mvn(org.apache.tomcat:tomcat-catalina) mvn(org.apache.tomcat:tomcat-el-api)
BuildRequires:       mvn(org.apache.tomcat:tomcat-jsp-api) mvn(org.apache.tomcat:tomcat-servlet-api)
BuildRequires:       mvn(org.apache.xmlbeans:xmlbeans) mvn(org.aspectj:aspectjweaver)
BuildRequires:       mvn(org.beanshell:bsh) mvn(org.codehaus.castor:castor-xml)
BuildRequires:       mvn(org.codehaus.groovy:groovy) mvn(org.codehaus.jackson:jackson-mapper-asl)
BuildRequires:       mvn(org.eclipse.jetty:jetty-server) mvn(org.eclipse.jetty:jetty-servlet)
BuildRequires:       mvn(org.eclipse.persistence:org.eclipse.persistence.core)
BuildRequires:       mvn(org.eclipse.persistence:org.eclipse.persistence.jpa)
BuildRequires:       mvn(org.freemarker:freemarker) mvn(org.hamcrest:hamcrest-core)
BuildRequires:       mvn(org.hibernate:hibernate-core:4) mvn(org.hibernate:hibernate-core:3)
BuildRequires:       mvn(org.hibernate:hibernate-entitymanager:4)
BuildRequires:       mvn(org.hibernate:hibernate-entitymanager:3)
BuildRequires:       mvn(org.hibernate:hibernate-validator)
BuildRequires:       mvn(org.hibernate.javax.persistence:hibernate-jpa-2.0-api)
BuildRequires:       mvn(org.hibernate.javax.persistence:hibernate-jpa-2.1-api)
BuildRequires:       mvn(org.jboss.spec.javax.resource:jboss-connector-api_1.7_spec)
BuildRequires:       mvn(org.jboss.spec.javax.resource:jboss-connector-api_1.6_spec)
BuildRequires:       mvn(org.jibx:jibx-run) mvn(org.jruby.extras:bytelist) mvn(org.jruby:jruby)
BuildRequires:       mvn(org.ow2.asm:asm) mvn(org.quartz-scheduler:quartz) mvn(org.slf4j:slf4j-api)
BuildRequires:       mvn(org.testng:testng) mvn(toplink.essentials:toplink-essentials)
BuildRequires:       mvn(velocity-tools:velocity-tools-view) mvn(velocity:velocity)
BuildRequires:       mvn(xmlunit:xmlunit) mvn(org.apache.taglibs:taglibs-standard-jstlel)
BuildRequires:       mvn(javax.servlet:jstl) mvn(org.apache.taglibs:taglibs-standard-spec)
BuildRequires:       mvn(com.jayway.jsonpath:json-path) mvn(net.sf.jopt-simple:jopt-simple) xmvn
BuildRequires:       jboss-jms-1.1-api jdo2-api jboss-ejb-3.1-api
Obsoletes:           springframework-instrument-tomcat < %{version}-%{release}
BuildArch:           noarch
%description
The spring is based on code pubilshed in Expert One-on-One J2EE Design and Dvelopment
by Rod Johnson (Wrox, 2002).it is a layered Java/J2ee application framework.

%package help
Summary:             Provides the Javadoc for springframework
Provides:            springframework-javadoc = %{version}-%{release}
Obsoletes:           springframework-javadoc < %{version}-%{release}

%description help
This help package provide the javadoc for springframework.

%package aop
Summary:             Provode the Spring Aspect Oriented Framework
%description aop
The package is an enabling technology,it allows the implementation of custom
aspects and provides declarative transaction management without EJB.

%package beans
Summary:             Provide the Spring Bean Factory
%description beans
The Package provides an advanced configuration mechanism capable of
managing beans of any nature, using potentially any kind of storage facility.

%package context
Summary:             Provide the Spring Application Context
%description context
The package is a complete superset of a bean factory, and
adds enhanced capabilities to it, some of them more J2EE and
enterprise-centric.

%package expression
Summary:             Spring Expression Language (SpEL)
%description expression
The package is a powerful expression
language that supports querying and manipulating an object graph at runtime.

%package instrument
Summary:             Spring Instrumentation
%description instrument
The Package exposes performance and
resource utilization metrics for the Spring container and
gives you runtime control of the container.

%package jdbc
Summary:             Spring JDBC
%description jdbc
The jdbc takes care of all the low-level details associated to the
development with JDBC.

%package jms
Summary:             Spring jms
%description jms
Spring jms provide Java Message Service 1.0.2/1.1 support.

%package orm
Summary:             Spring ORM
%description orm
Spring orm provide JDO support, JPA support, Hibernate
support, TopLink support.

%package orm-hibernate4
Summary:             Spring ORM Hibernate 4 Support
%description orm-hibernate4
orm-hibernate4 provide Hibernate 4 support.

%package oxm
Summary:             Spring OXM
%description oxm
This package provide marshaling and unmarshalling
for XML with JAXB context and JiBX binding factories.

%package devel
Summary:             Spring test context and MVC framework
Provides:            springframework-test = %{version}-%{release}
Provides:            springframework-test-mvc = %{version}-%{release}
Obsoletes:           springframework-test < %{version}-%{release}
Obsoletes:           springframework-test-mvc < %{version}-%{release}

%description devel
Spring's test MVC framework and Spring's test context framework. Also includes common Servlet and
Portlet API mocks.

%package tx
Summary:             Spring Transaction Management
%description tx
Spring provides a consistent abstraction for transaction management that
provides a consistent programming model across different transaction APIs,
supports declarative transaction management, provides a simpler API for
programmatic transaction management and integrates with Spring's various data
access abstractions.

%package web
Summary:             Spring Web
%description web
This package provide web application context, multipart
resolver, HTTP-based remoting support.

%prep
%autosetup -n spring-framework-3.2.18.RELEASE -p1
find -name "*.class" -delete
find -name "*.jar" -print -delete
cp %{SOURCE101} pom.xml
cp %{SOURCE102} spring-core/pom.xml
cp %{SOURCE103} spring-expression/pom.xml
cp %{SOURCE104} spring-context/pom.xml
cp %{SOURCE105} spring-aop/pom.xml
cp %{SOURCE106} spring-instrument/pom.xml
cp %{SOURCE107} spring-beans/pom.xml
cp %{SOURCE108} spring-orm/pom.xml
cp %{SOURCE109} spring-test/pom.xml
%pom_disable_module spring-instrument-tomcat
%pom_disable_module spring-context-support
%pom_disable_module spring-webmvc
%pom_disable_module spring-webmvc-portlet
%pom_disable_module spring-struts
cp %{SOURCE112} spring-jdbc/pom.xml
cp %{SOURCE113} spring-jms/pom.xml
cp %{SOURCE114} spring-tx/pom.xml
cp %{SOURCE115} spring-web/pom.xml
cp %{SOURCE116} spring-oxm/pom.xml
cp %{SOURCE120} spring-test-mvc/pom.xml
cp %{SOURCE121} spring-orm-hibernate4/pom.xml
sed -i "s|@VERSION@|3.2.18.RELEASE|" spring-orm-hibernate4/pom.xml
%pom_xpath_inject pom:modules "<module>spring-orm-hibernate4</module>"
%pom_change_dep -r org.hibernate: ::4 spring-orm-hibernate4
%pom_remove_dep :hibernate-entitymanager spring-orm
%pom_add_dep org.hibernate:hibernate-entitymanager:3 spring-orm
%pom_remove_dep :hibernate-core spring-orm
%pom_add_dep org.hibernate:hibernate-core:3 spring-orm
%pom_remove_dep javax.resource:connector-api spring-tx
%pom_add_dep org.jboss.spec.javax.resource:jboss-connector-api_1.7_spec spring-tx
%pom_remove_dep com.ibm.websphere:uow spring-tx
rm spring-tx/src/main/java/org/springframework/transaction/jta/WebSphereUowTransactionManager.java \
 spring-tx/src/test/java/org/springframework/transaction/jta/WebSphereUowTransactionManagerTests.java
%pom_remove_dep :hibernate-annotations spring-orm
%pom_remove_dep :hibernate-core spring-orm
%pom_add_dep org.hibernate:hibernate-core:3 spring-orm
rm -rf spring-orm/src/main/java/org/springframework/orm/ibatis/*
%pom_remove_dep :ibatis-sqlmap spring-orm
%pom_remove_dep :openjpa spring-orm
%pom_add_dep org.apache.openjpa:openjpa-lib spring-orm
%pom_add_dep org.apache.openjpa:openjpa-persistence spring-orm
%pom_remove_dep javax.resource:connector-api spring-jms
%pom_add_dep org.jboss.spec.javax.resource:jboss-connector-api_1.7_spec spring-jms
%pom_remove_dep hsqldb:hsqldb spring-jdbc
%pom_add_dep hsqldb:hsqldb:1 spring-jdbc
file = 'beans,web'
for p in ${file}; 
do
  %pom_remove_dep :el-api spring-${p}
  %pom_add_dep org.apache.tomcat:tomcat-el-api spring-${p}
done
%pom_remove_dep :persistence-api spring-context
%pom_add_dep org.hibernate.javax.persistence:hibernate-jpa-2.0-api spring-context
%pom_remove_dep :validation-api spring-context
%pom_add_dep org.apache.geronimo.specs:geronimo-validation_1.0_spec spring-context
%pom_add_dep org.apache.geronimo.specs:geronimo-interceptor_3.0_spec spring-context
%pom_add_dep org.jruby.extras:bytelist spring-context
%pom_remove_dep :persistence-api spring-orm
%pom_add_dep org.hibernate.javax.persistence:hibernate-jpa-2.0-api spring-orm
%pom_remove_dep javax.servlet:servlet-api spring-orm
%pom_add_dep org.apache.tomcat:tomcat-servlet-api spring-context
%pom_remove_dep :persistence-api spring-test
%pom_add_dep org.apache.tomcat:tomcat-el-api spring-test
%pom_remove_dep javax.servlet.jsp:jsp-api spring-test
%pom_add_dep org.apache.tomcat:tomcat-jsp-api spring-test
%pom_remove_dep -r javax.activation:activation
%pom_add_dep org.apache.taglibs:taglibs-standard-jstlel spring-test '<optional>true</optional>'
%pom_add_dep javax.servlet:jstl spring-web '<optional>true</optional>'
%pom_remove_dep taglibs:standard spring-web
rm spring-context/src/main/java/org/springframework/scripting/bsh/BshScriptFactory.java
rm spring-context/src/main/java/org/springframework/scripting/bsh/BshScriptUtils.java
%pom_remove_dep :backport-util-concurrent spring-context
%pom_add_dep org.ow2.asm:asm spring-core
%pom_add_dep net.sf.cglib:cglib:4.2 spring-core
%pom_xpath_set "pom:dependencies/pom:dependency[pom:groupId = 'org.codehaus.groovy']/pom:artifactId" groovy spring-context
find ./ -name "*.java" -exec sed -i "s/org.springframework.asm/org.objectweb.asm/g" {} +
find ./ -name "*.java" -exec sed -i "s/org.springframework.cglib/net.sf.cglib/g" {} +
find ./ -name "*.java" -exec sed -i "/edu.emory.mathcs.backport/d" {} +
%pom_change_dep -r :rome com.rometools: spring-test-mvc spring-web
find ./spring-test-mvc -name "*.java" -exec sed -i "s/com.sun.syndication/com.rometools.rome/g" {} +
find ./spring-web -name "*.java" -exec sed -i "s/com.sun.syndication/com.rometools.rome/g" {} +
rm spring-context/src/main/java/org/springframework/scheduling/backportconcurrent/*
cp -p src/dist/* .
mkdir -p spring-context/src/main/resources/org/springframework/remoting/rmi
cp -p spring-context/src/main/java/org/springframework/remoting/rmi/RmiInvocationWrapperRTD.xml \
 spring-context/src/main/resources/org/springframework/remoting/rmi/
mkdir -p spring-web/src/main/resources/org/springframework/web/context
cp -p spring-web/src/main/java/org/springframework/web/context/ContextLoader.properties \
 spring-web/src/main/resources/org/springframework/web/context/

for p in aop beans context core \
expression instrument jdbc jms orm oxm \
test test-mvc tx web; 
do
 %pom_xpath_inject "pom:project" "<packaging>bundle</packaging>" spring-${p}
 %pom_add_plugin org.apache.felix:maven-bundle-plugin:2.5.4 spring-${p} "
 <extensions>true</extensions>
 <configuration>
   <instructions>
     <Bundle-SymbolicName>\${project.groupId}.${p}</Bundle-SymbolicName>
     <Bundle-Name>\${project.name}</Bundle-Name>
     <Bundle-Version>\${project.version}</Bundle-Version>
   </instructions>
 </configuration>
 <executions>
   <execution>
     <id>bundle-manifest</id>
     <phase>process-classes</phase>
     <goals>
       <goal>manifest</goal>
     </goals>
   </execution>
 </executions>"
done
%pom_xpath_inject "pom:project" "<packaging>bundle</packaging>" spring-orm-hibernate4
%pom_add_plugin org.apache.felix:maven-bundle-plugin:2.5.4 spring-orm-hibernate4 "
<extensions>true</extensions>
 <configuration>
  <instructions>
    <Bundle-SymbolicName>\${project.groupId}.orm.hibernate4</Bundle-SymbolicName>
    <Bundle-Name>\${project.name}</Bundle-Name>
    <Bundle-Version>\${project.version}</Bundle-Version>
  </instructions>
 </configuration>
 <executions>
  <execution>
    <id>bundle-manifest</id>
    <phase>process-classes</phase>
    <goals>
      <goal>manifest</goal>
    </goals>
  </execution>
</executions>"
%mvn_package ":spring-core" springframework
%mvn_package :spring-project __noinstall

%build
%mvn_build -X -f -s -- -Dproject.build.sourceEncoding=ISO-8859-1 -Dmaven.test.skip=true

%install
%mvn_install  -- -Dmaven.test.skip=true

%files -f .mfiles-springframework
%license license.txt  notice.txt

%files help -f .mfiles-javadoc
%doc README.md
%license license.txt  notice.txt

%files aop -f .mfiles-spring-aop

%files beans -f .mfiles-spring-beans

%files context -f .mfiles-spring-context

%files expression -f .mfiles-spring-expression

%files instrument -f .mfiles-spring-instrument
%license license.txt  notice.txt

%files jdbc -f .mfiles-spring-jdbc

%files jms -f .mfiles-spring-jms

%files orm -f .mfiles-spring-orm

%files orm-hibernate4 -f .mfiles-spring-orm-hibernate4

%files oxm -f .mfiles-spring-oxm

%files tx -f .mfiles-spring-tx

%files web -f .mfiles-spring-web

%changelog
* Fri Oct 29 2021 houyingchao <houyingchao@huawei.com> - 3.2.18-8
- Fix CVE-2016-5007

* Thu Dec 17 2020 caodongxia <caodongxia@huawei.com> - 3.2.18-7
- Fix CVE-2020-5421

* Mon Oct 26 2020 huanghaitao <huanghaitao8@huawei.com> - 3.2.18-6
- Disable context-support webmvc module

* Tue Jun 9 2020 yaokai <yaoaki13@huawei.com> - 3.2.18-5
- package init
