import { Octokit } from "https://cdn.skypack.dev/@octokit/rest";

async function click() {
    console.log('ss')
    const octokit = new Octokit({
     auth: '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'
    });
    response = await octokit.request('POST /repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches', {
    owner: 'jkweil125',
    repo: 'github_action',
    workflow_id: 'learn-github-actions.yaml',
    ref: 'main',
    inputs: {
    name: 'Mona the Octocat',
    home: 'San Francisco, CA'
  }
})
console.log(response)
    
}
