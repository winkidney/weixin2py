<?php

// Page créé par Shepard [Fabian Pijcke] <Shepard8@laposte.net>
// et Romain Bourdon <romain@anaska.com>
// pour WAMP5 


//afficher phpinfo
if (isset($_GET['phpinfo']))
{
    phpinfo();
    exit();
}




// Définition de la langue et des textes 

if (isset ($_GET['lang']))
{
    $langue = $_GET['lang'];
}
elseif (preg_match("/^fr/", $_SERVER['HTTP_ACCEPT_LANGUAGE']))
{
    $langue = 'fr';
}
else
{
    $langue = 'en';
}
$langues = array(
    'en' => array(
        'langue' => 'English',
        'autre_langue' => 'version française',
        'autre_langue_lien' => 'fr',
        'titre_html' => 'WAMP5 Homepage',
        'titre_conf' => 'Server Configuration',
        'versa' => 'Apache version :',
        'versp' => 'PHP version :',
        'versm' => 'MySQL version :',
        'php_ext' => 'Loaded extensions : ',
        'titre_page' => 'Tools',
        'mysqlerror1' => 'MySQL not launched or bad phpmyadmin config',
        'mysqlerror2' => 'phpmyadmin connection not available',
        'txt_projet' => 'Your projects',
        'txt_no_projet' => 'No project yet.<br />To create a new one, just create a directory in \'www\'.',
        'txt_alias' => 'Your aliases',
        'txt_no_alias' => 'No Alias yet.<br />To create a new one, use the WAMP5 menu.',
        'faq' => 'http://www.en.wampserver.com/faq.php',


    ),
    'fr' => array(
        'langue' => 'Français',
        'autre_langue' => 'english version',
        'autre_langue_lien' => 'en',
        'titre_html' => 'Accueil WAMP5',
        'titre_conf' => 'Configuration Serveur',
        'versa' => 'Version de Apache:',
        'versp' => 'Version de PHP:',
        'versm' => 'Version de MySQL:',
        'php_ext' => 'Extensions chargées: ',
        'titre_page' => 'Outils',
        'mysqlerror1' => 'MySQL n\'est pas lanc&eacute; ou votre configuration phpmyadmin n\'est pas bonne.',
        'mysqlerror2' => 'connexion de phpmyadmin non disponible',
        'txt_projet' => 'Vos projets',
        'txt_no_projet' => 'Aucun projet.<br /> Pour en ajouter un nouveau, cr&eacute;ez simplement un r&eacute;pertoire dans \'www\'.',
        'txt_alias' => 'Vos alias',
        'txt_no_alias' => 'Aucun alias.<br /> Pour en ajouter un nouveau, utilisez le menu de WAMP5.',
        'faq' => 'http://www.wampserver.com/faq.php'
    ),
    'all' => array(
        'version' => '1.7.4',
        'phpmyadmin' => 'PHPmyadmin 2.11.2.1',
        'sqlitemanager' => 'SQLitemanager 1.2.0'
    )
);


// Version d'apache.
$apache_version = explode('PHP', apache_get_version());


// Version de MySQL.
$pma_conf_file = 'd:/wamp/phpmyadmin/'.'config.inc.php';
if (file_exists($pma_conf_file))
{
    include ($pma_conf_file);
    if (extension_loaded('mysql'))
    {
        if ($link = @mysql_connect('localhost',$cfg['Servers']['1']['user'] ,$cfg['Servers']['1']['password']))
	        $mysql_version =  mysql_get_server_info();
        else
	        $mysql_version = $langues[$langue]['mysqlerror1'];
    }
    if (extension_loaded('mysqli'))
    {
        if ($link = @mysqli_connect('localhost',$cfg['Servers']['1']['user'] ,$cfg['Servers']['1']['password']))
	        $mysql_version =  mysqli_get_server_info($link);
        else
	        $mysql_version = $langues[$langue]['mysqlerror1'];
    }
}
else
    $mysql_version = $langues[$langue]['mysqlerror2'];





echo '<?xml version="1.0" encoding="iso-8859-1"?>';

?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "xhtml11.dtd">

<html>
    <head>
        <title><?php echo $langues[$langue]['titre_html'] ?></title>
        <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
        <style type="text/css">
            .txtsouligne {text-decoration: underline;}
            .clearer { clear: both; }
            .clearer2 { clear: both; padding-top: 5px; border-bottom: groove #888888 3px; }
            DIV.all { width: 70%; border: groove #888888 3px; margin-left: auto; margin-right: auto; text-align: left; background-color: #EDEDED; padding: 0; font-family: Arial, Helvetica, sans-serif; font-size: 12px; font-style: normal; font-weight: normal; color: #000000;}
            DIV.cell { padding: 3px; }
            SPAN.header_bar { display: block; float: right; margin-top: 100px; }
            a:link { color: #003366; text-decoration: none; }
            a:hover { text-decoration: underline; color: #003366; }
            a:visited { color: #003366; text-decoration: none; }
            a:visited:hover { color: #003366; text-decoration: underline; }
            H1 { font-family: Arial, Helvetica, sans-serif; font-size: 14px; font-style: normal; font-weight: bold; text-decoration: underline; color: #000000; margin: 0; padding: 0; padding-left: 15px; padding-top: 15px; }
            DIV.content { padding-left: 30px; padding-top: 5px; }
            DIV.vitem { float: left; width: 250px; clear: both; }
            DIV.vright { float: left; padding-left: 20px; font-style: italic; width: 50%; }
            A.ditem { display: block; float: left; width: 500px; clear: both; }
            A.dright { float: left; padding-left: 50px; font-style: italic; width: 50%; }
            IMG { border: 0; }
            DIV.footer { font-size: 10pt; text-align: right; height: 28px; padding-right: 5px; vertical-align: top; }
        </style>
    </head>

    <body style="text-align: center;">
        <div class="all">
            <div class="cell">
                <img src="logo_i.gif" alt="logo" style="float: left;" />
                <span class="header_bar">Version 
                                <?php
                                echo $langues['all']['version'];
                                echo ' - <a href="?lang='.$langues[$langue]['autre_langue_lien'].'">'.$langues[$langue]['autre_langue'].'</a>';
                                ?>
                </span>
            </div>
            <div class="clearer2"></div>
            <div class="cell">
            </div>
            <h1><?php echo $langues[$langue]['titre_conf']; ?></h1>
            <div class="content">
                <div class="vitem"><?php echo $langues[$langue]['versa']; ?></div>
                <div class="vright"><?php echo $apache_version[0]; ?></div>
                <div class="vitem">&nbsp;</div>
		<div class="vitem"><?php echo $langues[$langue]['versp']; ?></div>
                <div class="vright"><?php echo phpversion(); ?></div>
                <div class="vitem">&nbsp;</div>
		<div class="vright"><div class="txtsouligne"><?php 
                echo $langues[$langue]['php_ext'].'</div>'; 
                
                $loaded_extensions = get_loaded_extensions();
                $separateur = '';
                foreach ($loaded_extensions as $extension)
                {
                    echo $separateur.$extension;
                    $separateur = ', ';
                }
                ?>
                </div>
                <div class="vitem">&nbsp;</div>
                <div class="vitem"><?php echo $langues[$langue]['versm']; ?></div>
                <div class="vright"><?php echo $mysql_version; ?></div>
            </div>
            <div class="clearer"></div>
            <h1><?php echo $langues[$langue]['titre_page']; ?></h1>
            <div class="content">
                <div class="vitem"><a href="?phpinfo=1">phpinfo( )</a></div>
                <div class="vitem"><a href="phpmyadmin/"><?php echo $langues['all']['phpmyadmin']; ?></a></div>
                <div class="vitem"><a href="sqlitemanager/"><?php echo $langues['all']['sqlitemanager']; ?></a></div>
            </div>
            <div class="clearer"></div>
            <h1><?php echo $langues[$langue]['txt_projet']; ?></h1>
            <div class="content">
                    <?php
                        // Affichage de la liste des dossiers non énumérés plus haut ( = projets ).
                        $list_ignore = array ('.','..','exemples','phpmyadmin','sqlitemanager');
                        $handle=opendir(".");

                        $msg = $langues[$langue]['txt_no_projet'];
                        while ($file = readdir($handle)) {
                            if (is_dir($file) && !in_array($file,$list_ignore)) {    
                                $msg = '';
                                echo '<a class="ditem" href="'.$file.'"><img src="dossier.gif" alt="image dossier" /> '.$file.'</a>';
                            }
                        }
                        closedir($handle);
                        echo $msg;
                    ?>
            </div>
            <div class="clearer">&nbsp;</div>
                        <h1><?php echo $langues[$langue]['txt_alias']; ?></h1>
            <div class="content">
                    <?php
                        
                        // Affichage des alias
                        $alias_dir = 'd:/wamp/apache2/conf/alias/';
                        $handle=opendir($alias_dir);

                        $msg = $langues[$langue]['txt_no_alias'];
                        while ($file = readdir($handle)) {
                            
                            if (is_file($alias_dir.$file) && ereg('.conf',$file)){    
                                $msg = '';
                                echo '<a class="ditem" href="'.ereg_replace('.conf','',$file).'/"><img src="dossier.gif" alt="image dossier" /> '.ereg_replace('.conf','',$file).'</a>';
                            }
                        }
                        closedir($handle);
                        echo $msg;
                    ?>
            </div>
            <div class="clearer">&nbsp;</div>
            <div class="clearer"></div>
            <hr />
            <div class="footer">
                <a href="<?php echo $langues[$langue]['faq']; ?>">faq</a>
                 - <a href="http://www.anaska.com">Powered by Anaska - created by Romain Bourdon</a>
            </div>
        </div>
    </body>
</html> 