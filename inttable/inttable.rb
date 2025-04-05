require 'json'
require 'fileutils'

# Global değişkenler
$RATER = nil
$LHOSTS = nil
$LPORTS = nil

# Banner fonksiyonu
def banner(hide = false)
  return if hide

  table = <<~BANNER
    ⠀⠀⠀⠀⣀⣀⣴⣶⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣠⣶⣆⣀⠀
    ⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ 
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠁
    ⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠛⢻⣿⡟⠛⠛⠛⠛⠛⠁⠀
    ⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡟⠻⣿⣶⠄⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣇⣀⣀⣁⣠⣾⡿⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⣼⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀inttable⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⢿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠈⠛⠿⠿⠿⠿⠿⠟⠀⠀⠀
  BANNER

  puts table
end

banner(true)

# Yazma fonksiyonu
def write(packet)
  File.open('.int4', 'a') { |file| file.puts packet }
end

# Console Sınıfı
class Console
  attr_reader :meta

  def initialize
    @meta = {
      author: '@intikam21',
      most_used: 'execute_command',
      int_commands: get_commands,
      parser: 'no parser!',
      var: 20
    }
  end

  def get_commands
    [
      'load_console_module', 'run_console_function', 'execute_command', 'use',
      'show_exploits', 'run_exploit', 'list_plugins', 'check', 'wifi_scan',
      'login', 'execute_get_input', 'run_exploit'
    ]
  end

  def run(packet)
    system("python3 $INTFRAMEWORK_PATH/remote.py #{packet}")
  end

  def prompt(pr)
    system("python3 intframework/intconsoleV4.py #{pr}")
  end

  def interactive
    system("python3 intframework/intconsoleV4.py")
  end

  def read
    File.read("intframework/intconsoleV4.py")
  end
end

# Modules Sınıfı
class Modules
  def use(mod)
    execute_command("use #{mod}")
  end

  def show_exploits
    execute_command("show exploits")
  end

  def execute_get_input(mod)
    system("python3 intframework/intconsoleV4.py #{mod}")
  end

  def login(username, password)
    system("python3 intframework/intconsoleV4.py #{username} #{password}")
  end

  def run_exploit
    execute_command("exploit")
  end

  def wifi_scan
    execute_command("wifi_scan")
  end

  def load_plugins(path)
    execute_command("load_plugins #{path}")
  end

  def run_plugins(cmd, *args)
    execute_command("run_plugins #{cmd} #{args.join(' ')}")
  end

  def list_plugins
    execute_command("list_plugins")
  end

  def check(ip)
    system("python3 intframework/intconsoleV4.py #{ip}")
  end
end

# Core Sınıfı
class Core
  def activate(rate)
    if rate.nil? || rate.empty?
      puts 'enter the rate please!'
    elsif rate == 'root'
      $RATER = 'root'
      puts 'user mod activated'
    elsif rate == 'dev'
      $RATER = 'dev'
      puts 'developer mode activated!'
    end
  end

  def console_exit
    exit
  end

  def pass_card; end
end

# Config Sınıfı
class Config
  def set(key, val)
    case key
    when 'LHOSTS'
      $LHOSTS = val
      puts "LHOSTS -> #{val}"
    when 'LPORTS'
      $LPORTS = val
      puts "LPORTS -> #{val}"
    else
      puts "#{key} -> #{val}"
    end
  end
end

# Exploit Sınıfı
class Exploit
  def run(dir, exp, args = nil)
    puts "running #{exp}"
    Dir.chdir('$intmodules_path/exploits') do
      system("cd #{dir} && python3 #{exp} #{args}")
    end
  end

  def shell
    system("cd $intmodules_path/exploits/multi/handler && python3 inthandler.py")
  end
end

# execute_command fonksiyonu
def execute_command(cmd)
  system("python3 intframework/intconsoleV4.py \"#{cmd}\"")
end