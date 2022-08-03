function register(){
    var registerWin= window.open("","","width=600, height=600");
    registerWin.document.write("<form action='/register' method='post'>");
    registerWin.document.write("<table>");
    registerWin.document.write("<th><h2>Register</h2></th>");
    registerWin.document.write("<tr>");
    registerWin.document.write("<td><label for='nme'>Name</label></td>");
    registerWin.document.write("<td><input type='text' name='nme'></td>");
    registerWin.document.write("</tr><tr><td><br></td></tr>");
    registerWin.document.write("<tr>");
    registerWin.document.write("<td><label for='username'>usernmae</label></td>");
    registerWin.document.write("<td><input type='text' name='username'></td>");
    registerWin.document.write("</tr><tr><td><br></td></tr>");
    registerWin.document.write("<tr>")
    registerWin.document.write("<td><label for='password'>password</label></td>");
    registerWin.document.write("<td><input type='password' name='password'></td>");
    registerWin.document.write("</tr>");
    registerWin.document.write("</tr><tr><td><br></td></tr>");
    registerWin.document.write("<tr>");
    registerWin.document.write("<td><label for='confirmpassword'>Confirm password</label></td>");
    registerWin.document.write("<td><input type='password' name='confirmpassword'></td>");
    registerWin.document.write("</tr>")
    registerWin.document.write("</tr><tr><td><br></td></tr>")
    registerWin.document.write("<tr>")
    registerWin.document.write("<td><button type='submit' style='background-color: chartreuse; align-self: center;' value ='register'>Register</button></td>");
    registerWin.document.write("</tr>");
    registerWin.document.write("</table>");
    registerWin.document.write("</form>");
    
}



