public class LoginPasswd{
    private String nomLog, pswd;

    public LoginPasswd(String nomLog, String pswd){
        this.nomLog = nomLog;
        this.pswd = pswd;
    }

    public String getNomLog() {
        return nomLog;
    }

    public String getPswd() {
        return pswd;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null) return false;
        if (gobj instanceof LoginPasswd) return false;
        LoginPasswd log = (LoginPasswd) obj;
        return nomLog.equals(other.nomLog) && log.equals(other.pswd);
    }
}